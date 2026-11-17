# GymFlow — Campus Gym Crowd Monitoring

GymFlow is a lightweight Python and Streamlit prototype for helping students and faculty at NIT Jamshedpur check reported gym crowd levels before visiting. It shows current occupancy, remaining capacity, a green/yellow/red crowd indicator, the approved operating timetable, and historical crowd patterns from uploaded CSV or Excel observations.

**GymFlow is not a booking system.** Users view the displayed information and decide when to visit. An attendant updates the current count when someone enters or leaves.

> **Fieldwork status:** A 20-minute visit and a conversation with a student have been documented in [`fieldwork.md`](fieldwork.md), with two selected photographs in [`photos/`](photos/). The real-observation file is [`data.csv`](data.csv), which currently contains only its header. At least 20 genuine, personally measured rows are still required before final submission.

## Problem and intended users

The project investigates crowding, waiting for occupied equipment, and uncertainty about which periods are less busy in the NIT Jamshedpur gym. Intended users are students and faculty checking availability, and the gym attendant/authorized administrator maintaining the count.

The reported operating windows are 4:00 AM–9:00 AM and 4:00 PM–9:00 PM; confirm these with the gym authority. Any separate student/faculty timings shown in the prototype are illustrative until officially confirmed.

## MVP features

- Current people count, approved capacity, available spaces, and occupancy percentage.
- Green/yellow/red crowd status using configurable thresholds.
- Operating-hours and approved timetable display.
- Manual attendant entry/exit counter with bounds checks.
- Local JSON state and timestamped CSV event log; no external database.
- CSV/Excel upload, data validation, historical occupancy chart, averages, and observed busiest/quietest records.

The prototype does not provide reservations, automatic people detection, biometric access, or multi-device real-time synchronization.

## Technology

- Python
- Streamlit
- Pandas
- Plotly
- OpenPyXL
- Local JSON and CSV files

## Run locally

Requires Python 3.11 or newer.

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies and start the application:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Open the local URL printed by Streamlit (normally `http://localhost:8501`).

## Observation data format

Upload a `.csv` or `.xlsx` file with these columns:

```text
timestamp,people_present,equipment_in_use,equipment_total,waiting_people
```

- `timestamp`: date and time of the observation
- `people_present`: people physically inside the gym
- `equipment_in_use`: equipment units currently in use
- `equipment_total`: total usable equipment units counted
- `waiting_people`: people waiting for equipment or space, using a consistent counting rule

The application validates required columns, timestamps, numeric values, non-negative counts, occupancy against the configured capacity, and equipment usage against the equipment total.

## Data files and integrity

- `data.csv` is reserved for actual fieldwork observations and is the dashboard's default historical-data source. It is currently a header-only template and must be filled with at least 20 genuine measured rows before submission.
- `data/gymflow_demo_sample.xlsx` and `data/gym_observations_sample.csv` are synthetic/development examples. They are for software testing only and must never be described as fieldwork.
- Uploaded historical files are analysed in memory and are not permanently stored by the application.

Do not place identifiable student information or private attendance registers in this public repository.

## Local runtime storage

- `data/current_state.json` stores the latest manually maintained occupancy count and capacity.
- `data/attendance_log.csv` stores timestamped entry/exit actions without personal identifiers.

These mutable runtime files are excluded from Git by `.gitignore`. The local-file design is intended for a single-computer demonstration; it does not synchronize attendants on different devices.

## Fieldwork evidence

See [`fieldwork.md`](fieldwork.md) for the visit notes, student conversation summary, data-collection method, and outstanding checks.

Selected photographs:

- [Gym environment](photos/gym_environment_2026-11-17_21-45-56.jpeg)
- [Gym equipment](photos/gym_equipment_2026-11-17_21-45-57.jpeg)

The image filenames indicate a time around 9:45 PM, which appears later than the reported 9:00 PM closing time. Verify the original capture times and clarify this before final submission. Identifiable people should only be published with permission.

## Testing

```bash
pytest
```

## Demo

Watch the completed [three-minute GymFlow demonstration on Google Drive](https://drive.google.com/file/d/1z-ZTo5msltKrELBMjvSG-ehgOuhvMF5b/view?usp=sharing). The narration and click-by-click plan are in [`demo/video-script.md`](demo/video-script.md).

## AI assistance

ChatGPT was used as an assistant for planning, implementation support, testing ideas, and documentation. The [AI assistance record](ai-chats/conversations.md) includes the [shared ChatGPT conversation](https://chatgpt.com/share/6afca28e-6b14-83ee-8dd7-42e26a69bffc).

## Limitations

- Current occupancy depends on the attendant recording each entry and exit accurately.
- Historical analysis describes only the periods included in the uploaded observations; it does not predict unobserved peak hours.
- Capacity, colour thresholds, opening hours, and student/faculty session allocations must be confirmed with the gym authority.
- Local JSON/CSV files are not a secure multi-user database and are not suitable for concurrent multi-device updates.
- This prototype is not an official access-control or safety system.

## Important submission files

- [Research and initial problem definition](research.md)
- [Fieldwork notes, interview summary, and data-collection method](fieldwork.md)
- [Personal reflection](reflection.md)
- [Real fieldwork dataset - add at least 20 genuine rows before submission](data.csv)
- [Selected gym environment photo](photos/gym_environment_2026-11-17_21-45-56.jpeg)
- [Selected gym equipment photo](photos/gym_equipment_2026-11-17_21-45-57.jpeg)
- [All gym photographs](photos/)
- [Three-minute application demonstration](https://drive.google.com/file/d/1z-ZTo5msltKrELBMjvSG-ehgOuhvMF5b/view?usp=sharing)
- [ChatGPT assistance record and conversation link](ai-chats/conversations.md)
