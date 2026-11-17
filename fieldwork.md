# Fieldwork: NIT Jamshedpur Gym Crowd Monitoring

> **Status: Partially complete.** The 20-minute visit, student conversation and two selected photographs are documented. The required dataset of at least 20 genuine measured observations is not complete in the CSV supplied here. Administrative details and original photo timestamps also need confirmation.

## 1. Visit Details

- **Place:** Gymkhana Gym, NIT Jamshedpur, Jharkhand, India
- **Date reported:** 17 November 2026
- **Observation duration:** 20 minutes
- **Person spoken to:** Shyam Kumar (confirm permission before publishing his name publicly)
- **Role:** Student and gym user
- **Conversation method:** Face-to-face conversation; no interview video was recorded.

## 2. What I Observed

The photographs show the gym's indoor workout area and equipment, including dumbbells, weight plates, benches and weight machines. The gym contains several types of workout equipment within the available indoor space.

The concerns reported during the visit and student conversation were:

1. **Crowding:** When multiple people use the gym at the same time, users may find it difficult to exercise comfortably.
2. **Waiting for equipment:** Equipment may already be occupied, so a student has to wait and may lose part of the planned workout time.
3. **Entry/exit and registration:** The student raised concerns about the organisation of gym registration and records of people entering and leaving. The exact current process still needs to be confirmed with the gym attendant.

The photographs document the gym environment and equipment. They do not, by themselves, establish the approved capacity, exact room dimensions, peak-hour pattern or occupancy over time.

## 3. Conversation with a Student

- **Interviewee:** Shyam Kumar (public identification permission to be confirmed)
- **Role:** Student who uses the gym
- **Conversation method:** Face-to-face conversation

The following are paraphrases of the conversation as recalled and reported by me, not verbatim quotations:

1. Shyam described overcrowding as a difficulty when many students come to exercise at the same time.
2. He said equipment is sometimes occupied, which makes users wait and reduces the time available for their workouts.
3. He raised concerns about the organisation of gym registration and the recording of people entering and leaving.

### One thing that surprised me

I was surprised to learn that students cannot reliably predict which period will be less crowded. A student may expect the morning to be quieter but sometimes find more people exercising than expected. This uncertainty makes it difficult to choose a suitable visiting time based only on assumptions about the schedule.

## 4. Photographic Evidence

Two photographs from the visit are included in `photos/`:

- **Photo 1 – Gym environment:** `photos/gym_environment_2026-11-17_21-45-56.jpeg` — shows the entrance area and weights on the gym floor.
- **Photo 2 – Equipment:** `photos/gym_equipment_2026-11-17_21-45-57.jpeg` — shows a weight machine and nearby workout equipment.

The filenames supplied with the images indicate approximately 9:45 PM on 17 November 2026. The shared copies did not provide readable EXIF capture-time metadata. This appears later than the stated 9:00 PM closing time, so the original phone-gallery capture times and the gym's hours on that date must be checked before final submission. Do not change or invent timestamps.

These selected photographs avoid showing identifiable gym users. If other photographs showing people are added to the public repository, obtain their permission or blur/crop them first.

## 5. Data Collection

- **Required dataset:** At least 20 genuine observations collected personally at the gym.
- **File:** `data/gym_observations_real.csv`
- **Columns:** `timestamp`, `people_present`, `equipment_in_use`, `equipment_total`, `waiting_people`
- **Collection method:** At each observation, record the actual number of people inside, the number of equipment units in use, the total usable equipment units and the number of people waiting. Apply the same counting rules each time and do not record personal identifiers.

**Current status: Partially collected, not submission-ready.** The CSV currently contains only its header because no measured rows were supplied for this repository update. Add the observations you actually recorded and continue until at least 20 complete, genuine rows are present. Do not copy synthetic development data into this file.

## 6. Remaining Fieldwork Checks

- [x] Record the reported visit location and date.
- [x] Record a 20-minute observation duration.
- [x] Record the student interviewee's name and role as provided.
- [x] Document three conversation findings as paraphrases.
- [x] Document the surprising finding about uncertainty in morning crowd levels.
- [x] Include two selected photographs of the gym environment and equipment.
- [ ] Confirm Shyam Kumar is comfortable being named in the public repository.
- [ ] Verify the original photo capture times and clarify the apparent difference from the stated closing time.
- [ ] Speak with the gym attendant/guard to confirm how entry, exit and attendance are currently managed.
- [ ] Confirm the actual opening hours and any student/faculty access arrangements with the gym authority.
- [ ] Confirm the approved maximum occupancy with the responsible authority; do not infer capacity from room size.
- [ ] Add at least 20 genuine, timestamped observation rows to `data/gym_observations_real.csv`.

## 7. Implications for GymFlow

The initial fieldwork suggests that GymFlow should help users understand reported crowd conditions before they visit. The MVP will focus on:

- Showing the manually updated number of people inside and the remaining capacity.
- Displaying green, yellow or red crowd status using thresholds confirmed by the gym administration.
- Showing confirmed opening hours and any officially approved student/faculty timings.
- Letting the attendant record entries and exits through a simple counter.
- Analysing genuine historical observations to show crowd levels during the periods actually measured.

Student/faculty schedules, occupancy limits and the current registration process must be confirmed with the gym authority. GymFlow will not include booking or reservations.
