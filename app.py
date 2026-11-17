"""GymFlow: a lightweight campus gym crowd monitor."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

from src.counter import load_state, set_capacity, update_count
from src.data_loader import DataLoadError, load_observations, load_sample_data
from src.occupancy import available_spaces, crowd_status, historical_summary, occupancy_percentage
from src.validation import REQUIRED_COLUMNS, validate_observations


PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"
STATE_PATH = DATA_DIR / "current_state.json"
LOG_PATH = DATA_DIR / "attendance_log.csv"
SAMPLE_PATH = DATA_DIR / "gymflow_demo_sample.xlsx"


st.set_page_config(page_title="GymFlow", page_icon="🏋️", layout="wide")


def inject_styles() -> None:
    st.markdown(
        """
        <style>
          .stApp { background: #f7f8fc; color: #162033; }
          [data-testid="stHeader"] { background: rgba(0,0,0,0); }
          .stApp p, .stApp li, .stApp label, .stApp span, .stApp small,
          .stApp [data-testid="stMarkdownContainer"] { color: #283548; }
          .stApp h1, .stApp h2, .stApp h3, .stApp h4,
          .stApp [data-testid="stMetricLabel"] p,
          .stApp [data-testid="stMetricValue"] { color: #162033; }
          .stApp [data-testid="stCaptionContainer"] p { color: #667085; }
          button[data-baseweb="tab"] { color: #475467 !important; font-weight: 600; }
          button[data-baseweb="tab"][aria-selected="true"] { color: #175CD3 !important; }
          .hero { padding: 1.3rem 0 .4rem; }
          .hero h1 { margin: 0; color: #11243d; font-size: 2.7rem; letter-spacing: -0.07rem; }
          .hero p { color: #596579; font-size: 1.06rem; margin: .45rem 0 0; }
          .status-card { border-radius: 18px; padding: 1.2rem 1.35rem; color: #ffffff; min-height: 133px; }
          .status-card h2 { margin: 0; color: #ffffff !important; font-size: 1.65rem; }
          .status-card p { margin: .55rem 0 0; color: #ffffff !important; font-size: 1rem; opacity: .94; }
          .green { background: linear-gradient(135deg, #067647, #149d67); }
          .yellow { background: linear-gradient(135deg, #9d6500, #db941a); }
          .red { background: linear-gradient(135deg, #b42318, #e45248); }
          div[data-testid="stMetric"] { background: #ffffff; padding: 1rem; border-radius: 14px; border: 1px solid #d0d5dd; }
          div[data-testid="stMetric"] * { color: #162033; }
          div[data-testid="stAlert"] p { color: inherit; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def load_dashboard_data() -> tuple[pd.DataFrame, str]:
    """Return uploaded data for this session, or bundled development data."""
    uploaded = st.session_state.get("observations")
    if uploaded is not None:
        return uploaded.copy(), "Uploaded dataset"
    return load_sample_data(SAMPLE_PATH), "Bundled development sample"


def render_dashboard(state: dict[str, int | str | None]) -> None:
    people, capacity = int(state["people_present"]), int(state["capacity"])
    status = crowd_status(people, capacity)
    percentage = occupancy_percentage(people, capacity)
    spaces = available_spaces(people, capacity)

    st.markdown('<section class="hero"><h1>GymFlow</h1><p>Campus gym availability, at a glance.</p></section>', unsafe_allow_html=True)
    st.caption("Live count is updated manually by the attendant. It is not automated people detection.")
    metrics, status_column = st.columns([3, 1.45])
    with metrics:
        one, two, three = st.columns(3)
        one.metric("People inside", people, f"of {capacity} capacity")
        two.metric("Available spaces", spaces)
        three.metric("Occupancy rate", f"{percentage:.0f}%")
    with status_column:
        st.markdown(
            f'<div class="status-card {status.colour}"><h2>{status.label}</h2><p>{status.message}</p></div>',
            unsafe_allow_html=True,
        )

    st.divider()
    left, right = st.columns([1.7, 1])
    with left:
        st.subheader("Operating hours")
        schedule = pd.DataFrame(
            [
                {"Group": "Students", "Morning": "6:00 AM – 8:30 AM", "Evening": "4:30 PM – 8:00 PM"},
                {"Group": "Faculty", "Morning": "8:30 AM – 10:00 AM", "Evening": "3:30 PM – 4:30 PM"},
            ]
        )
        st.dataframe(schedule, hide_index=True, use_container_width=True)
        st.caption("Illustrative timetable — confirm with the gym authority before deployment.")
    with right:
        st.subheader("How to read the indicator")
        st.success("Available: below 50%")
        st.warning("Moderate: 50%–84%")
        st.error("Busy: 85% or more")

    st.divider()
    st.subheader("Historical crowd patterns")
    observations, source = load_dashboard_data()
    report = validate_observations(observations, capacity)
    st.caption(f"Source: {source}")
    if not report.is_valid:
        st.error("The selected historical dataset cannot be analysed.")
        for error in report.errors:
            st.write(f"• {error}")
        return

    chart_data = observations.copy()
    chart_data["timestamp"] = pd.to_datetime(chart_data["timestamp"])
    chart_data = chart_data.sort_values("timestamp")
    summary = historical_summary(chart_data, capacity)
    chart, summary_column = st.columns([2, 1])
    with chart:
        figure = px.line(
            chart_data,
            x="timestamp",
            y="people_present",
            markers=True,
            labels={"timestamp": "Observation time", "people_present": "People present"},
            color_discrete_sequence=["#375dfb"],
        )
        figure.add_hline(y=capacity, line_dash="dash", line_color="#d92d20", annotation_text="Capacity")
        figure.update_layout(height=330, margin=dict(l=5, r=5, t=20, b=5), plot_bgcolor="white", paper_bgcolor="white")
        st.plotly_chart(figure, use_container_width=True)
    with summary_column:
        st.metric("Average crowd", f"{summary['average_people']} people")
        st.metric("Average occupancy", f"{summary['average_occupancy']}%")
        st.write(f"**Busiest observed:** {summary['busiest_people']} people")
        st.caption(summary["busiest_timestamp"])
        st.write(f"**Quietest observed:** {summary['quietest_people']} people")
        st.caption(summary["quietest_timestamp"])


def render_attendant_panel(state: dict[str, int | str | None]) -> None:
    st.subheader("Attendant console")
    st.write("Update the live count when one person enters or leaves. Every update is timestamped locally.")
    count_column, controls = st.columns([1, 2])
    with count_column:
        st.metric("Current count", f"{state['people_present']} / {state['capacity']}")
        if state.get("updated_at"):
            st.caption(f"Last updated: {state['updated_at']}")
    with controls:
        enter, leave = st.columns(2)
        if enter.button("+ Person enters", type="primary", use_container_width=True):
            try:
                update_count(STATE_PATH, LOG_PATH, 1)
                st.rerun()
            except ValueError as error:
                st.error(str(error))
        if leave.button("− Person leaves", use_container_width=True):
            try:
                update_count(STATE_PATH, LOG_PATH, -1)
                st.rerun()
            except ValueError as error:
                st.error(str(error))

    st.divider()
    st.subheader("Capacity setting")
    st.caption("Set this only after the gym authority confirms the practical capacity.")
    with st.form("capacity_form"):
        new_capacity = st.number_input("Confirmed capacity", min_value=1, value=int(state["capacity"]), step=1)
        if st.form_submit_button("Save capacity"):
            try:
                set_capacity(STATE_PATH, int(new_capacity))
                st.success("Capacity saved.")
                st.rerun()
            except ValueError as error:
                st.error(str(error))


def render_data_panel(capacity: int) -> None:
    st.subheader("Historical observation data")
    st.write("Upload a CSV or XLSX file to analyse genuine field observations. The upload is used only in this browser session.")
    st.code(", ".join(REQUIRED_COLUMNS), language="text")
    uploaded = st.file_uploader("Observation file", type=["csv", "xlsx"], label_visibility="collapsed")
    if uploaded is not None:
        try:
            observations = load_observations(uploaded)
            report = validate_observations(observations, capacity)
            if report.is_valid:
                st.session_state["observations"] = observations
                st.success(f"{len(observations)} valid observations loaded. Open Dashboard to review the analysis.")
                st.dataframe(observations, hide_index=True, use_container_width=True)
            else:
                st.error("The file was read but contains validation errors.")
                for error in report.errors:
                    st.write(f"• {error}")
        except DataLoadError as error:
            st.error(str(error))

    if st.button("Use bundled development sample"):
        st.session_state.pop("observations", None)
        st.success("Using the bundled development-only sample data.")

    st.info("The bundled sample is synthetic and must be replaced with personally collected observations for assignment submission.")


def main() -> None:
    inject_styles()
    try:
        state = load_state(STATE_PATH)
    except ValueError as error:
        st.error(str(error))
        st.stop()

    dashboard, attendant, data = st.tabs(["Dashboard", "Attendant", "Data upload"])
    with dashboard:
        render_dashboard(state)
    with attendant:
        render_attendant_panel(state)
    with data:
        render_data_panel(int(state["capacity"]))


if __name__ == "__main__":
    main()
