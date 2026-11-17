# GymFlow — 3-minute video script

Before recording, run `./run_app.ps1`, open `http://localhost:8501`, and make sure the **Dashboard** tab is visible. Record only the browser window. The included Excel sheet is development-only; say that clearly in the recording.

## 0:00–0:25 — Problem and dashboard

**Show:** Dashboard title and the four occupancy cards.

**Narration:**

“This is GymFlow, a campus gym crowd-monitoring tool. It helps students and faculty decide when to visit by showing the current number of people inside, the remaining capacity, occupancy percentage, and a simple crowd status. It is not a booking or face-recognition system.”

## 0:25–0:50 — Crowd indicator and timetable

**Show:** Available/Moderate/Busy card, then scroll to the timetable.

**Narration:**

“The status uses green for available, yellow for moderate, and red for busy. The timetable is shown beside the indicator so visitors can check the proposed operating times. These values are prototype settings and need confirmation from the gym authority.”

## 0:50–1:30 — Attendant controls

**Click:** **Attendant** tab. Click **+ Person enters**, pause to show the changed count, then click **− Person leaves**.

**Narration:**

“The live count is maintained by the attendant. When someone enters or leaves, the attendant uses these controls. GymFlow prevents an exit below zero and an entry above the configured capacity. Each successful action is saved locally with a timestamp for a simple audit trail.”

## 1:30–1:50 — Capacity rule

**Show:** Capacity setting; do not change it unless a real capacity is known.

**Narration:**

“The capacity can be changed only after the gym authority confirms a practical limit. The tool also prevents setting a capacity lower than the number already inside.”

## 1:50–2:30 — Excel upload and validation

**Click:** **Data upload** tab. Select `data/gymflow_demo_sample.xlsx`.

**Narration:**

“For historical analysis, the administrator can upload a CSV or Excel file. The required fields are timestamp, people present, equipment in use, total equipment, and waiting people. The application checks for missing columns, invalid timestamps, negative values, occupancy above capacity, and impossible equipment totals.”

## 2:30–2:50 — Historical insight

**Click:** **Dashboard** tab and scroll to the chart.

**Narration:**

“After valid data is loaded, GymFlow plots the crowd pattern and summarises the average crowd plus the busiest and quietest observed periods. This Excel sheet is synthetic development data, not real fieldwork.”

## 2:50–3:00 — Close

**Show:** Dashboard summary.

**Narration:**

“The next step is to replace the sample file with genuine observations, confirm the capacity and timetable, and collect feedback from the gym attendant. Thank you.”
