# GymFlow — 3-minute screen-recording guide

Start the app with `./run_app.ps1`, then open `http://localhost:8501` in a browser. Record only the browser window and keep the narration focused on what the tool actually does.

| Time | Show | Say |
| --- | --- | --- |
| 0:00–0:20 | Dashboard title and live occupancy cards | “GymFlow helps campus gym users check crowd conditions before they visit. This count is maintained manually by the attendant.” |
| 0:20–0:45 | Available spaces, occupancy rate and colour status | “The dashboard shows people inside, available space and a clear green, yellow or red crowd indicator. The thresholds are configurable after the authority confirms capacity.” |
| 0:45–1:05 | Operating-hours table | “Students and faculty can also see the current approved timetable. These displayed times are prototype values and should be confirmed by the gym authority.” |
| 1:05–1:40 | Attendant tab; click **Person enters**, then **Person leaves** | “The attendant records each entry or exit. GymFlow prevents counts below zero or above capacity, and saves an audit record locally.” |
| 1:40–2:10 | Capacity setting | “The capacity can be set when a practical limit is confirmed. The system will not allow the capacity to be lower than the people already inside.” |
| 2:10–2:35 | Data upload tab; upload `data/gymflow_demo_sample.xlsx` | “Historical data can be uploaded as an Excel or CSV file. GymFlow validates timestamps, required fields, negative values, capacity, and equipment totals.” |
| 2:35–2:55 | Dashboard historical chart and summary | “The dashboard plots crowd trends and identifies the busiest and quietest observed periods. The included Excel file is clearly synthetic development data.” |
| 2:55–3:00 | Dashboard | “For final submission, this development sample will be replaced with genuine field observations. GymFlow does not make bookings or use face recognition.” |

## Recording steps

1. Use Windows Game Bar (`Win` + `G`) or another screen-recorder to record the browser window.
2. Record at 1080p if possible, with microphone narration enabled.
3. Save the file as `gymflow-demo.mp4` in a shareable location such as Google Drive or YouTube (unlisted).
4. Paste the share link in `demo-link.txt`.
