# Reflection

At the start, I made the project broader than it needed to be. I initially thought about slots and booking, but the real problem is simpler: people need a quick way to see how crowded the gym is before they visit. I also assumed too much about the gym's capacity and timetable. These values must be confirmed with the gym authority, so the application now treats them as editable prototype settings rather than facts.

If I rebuilt the project, I would cut any feature that does not directly help with crowd visibility. I would not add user accounts, payments, reservations, face recognition, or fitness tracking. For this first version, a manual attendant counter and a small historical dataset are enough to demonstrate the idea clearly.

AI helped me organise the project structure, write repetitive validation code, improve the dashboard's visual contrast, and prepare test cases and documentation. It also saved time when explaining how CSV/Excel upload and local JSON/CSV storage could work together.

AI also wasted time when the scope became too detailed before the core dashboard was complete. The most useful progress came from building the smallest working version first: current occupancy, crowd status, entry/exit controls, and historical analysis. The next important step is not adding more code; it is collecting genuine gym observations, confirming the capacity and timetable, and getting feedback from the gym attendant.
