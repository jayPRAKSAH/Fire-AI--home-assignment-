# GymFlow — Campus Gym Crowd Monitor

GymFlow is a small Streamlit application for showing a gym's manually updated occupancy, remaining capacity, crowd indicator, operating timetable and historical observation trends.

It is deliberately not a booking platform: students and faculty check availability, while an attendant maintains the live count with simple entry/exit controls.

## Features

- Current people count, remaining spaces and occupancy rate
- Available / Moderate / Busy indicator (green, yellow and red)
- Configurable capacity with safeguards against impossible counts
- Timestamped, local attendant audit log
- CSV and Excel (`.xlsx`) historical-data upload
- Dataset validation with clear row-level errors
- Historical crowd chart, averages, and busiest/quietest observed periods

## Run locally

Requires Python 3.11 or newer.

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Open the local URL printed by Streamlit.

On the prepared Windows environment, you can also run:

```powershell
.\run_app.ps1
```

Then visit `http://localhost:8501`. The narrator's three-minute demo script is in [`demo/recording-guide.md`](demo/recording-guide.md).

## Data format

Upload a CSV or XLSX file with exactly these fields:

```text
timestamp,people_present,equipment_in_use,equipment_total,waiting_people
```

GymFlow rejects missing values, invalid timestamps, negative values, occupancy above the configured capacity and equipment usage above the equipment total.

`data/gymflow_demo_sample.xlsx` is a synthetic Excel development dataset included for exercising the upload path. It must be replaced with genuine, personally collected observations before an academic submission; do not present it as fieldwork.

## Storage

This MVP does not use an external database. It creates two local files at runtime:

- `data/current_state.json` — latest live count and capacity
- `data/attendance_log.csv` — timestamped entry and exit actions

Those mutable files are gitignored. Uploaded historical files are analysed in memory and are not retained by the application.

## Verification

```bash
pytest
```

The included tests cover the occupancy thresholds, uploaded-data validation and counter capacity boundaries.

## Limitations

- The live count depends on accurate manual updates; GymFlow does not use cameras, face recognition or automatic people detection.
- Historical insights describe only the observation periods contained in the uploaded dataset.
- The capacity and operating timetable shown in the UI are prototype defaults and must be confirmed by the gym authority.

See [research.md](research.md) for the initial research and fieldwork plan.
