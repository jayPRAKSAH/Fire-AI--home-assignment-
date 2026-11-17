# Research: NIT Jamshedpur Gym Crowd Management

## 1. Problem Statement

The gymnasium at NIT Jamshedpur has limited floor space (estimated at approximately 10 ft × 10 ft) and is shared by B.Tech, M.Tech, MCA and PhD students, as well as faculty members.

Due to limited space and a large number of users, the gym may become overcrowded, especially when several students arrive at the same time.

This can create several problems:
- Users may have to wait for available equipment.
- Limited space may make exercising uncomfortable.
- Students may not be able to complete their planned workouts.
- Some users may leave without finishing their sessions.
- Users may not know the current crowd level or the best time to visit.
- The administration may not have organized digital records of gym usage.

**My Objective:**

I aim to address these problems by developing a **Campus Gym Slot Booking and Crowd Management System** that allows users to check gym availability, book suitable time slots and maintain digital attendance records.

The system may also support separate schedules for different user groups, depending on the actual requirements and rules approved by the gym administration.

### Basic Information

| Detail | Information |
|---|---|
| Location | Gymkhana Gym, NIT Jamshedpur, Jharkhand, India |
| Date First Identified | 17 November 2026 |
| Affected People | Students, faculty members and gym guard/attendant |
| Main Concern | Gym overcrowding and difficulty managing gym usage |

**People Affected:**

The main people affected are students and faculty members who use the gym. The gym guard/attendant may also be affected because they help manage access to the facility.

I will record the name and role of the person I speak with during fieldwork.

### Current Situation

I have not yet confirmed how the gym currently manages entry, attendance or busy hours.

During my visit, I will speak with the guard/attendant and observe how people use the available space and equipment.

I will record only information that I personally observe or that people share with me. I will not assume that the gym uses a paper register, fixed time slots or any other particular system without confirming it.

## 2. Existing Solutions

I researched two existing gym-management platforms to understand how other gyms manage bookings, attendance and crowd levels.

### Solution 1: Gymdesk – Online Gym Booking

**What it does:**
- Allows members to book gym sessions online.
- Allows administrators to set the maximum number of people per session.
- Supports booking rules and waiting lists when a session is full.

**Why it may not fit our situation:**

Gymdesk is a general gym-management platform. The NIT Jamshedpur gym may need a simpler system designed specifically for a college environment.

The system would need to follow the gym's actual capacity and college-approved access rules. I will compare these requirements with feedback from the guard/attendant before deciding what features are necessary.

### Solution 2: MyGymDesk – Gym Management Platform

**What it does:**
- Supports QR-code and biometric attendance.
- Provides class scheduling and slot booking.
- Includes capacity management and member records.
- Also offers features such as billing and membership management.

**Why it may not fit our situation:**

The main requirements of the NIT gym may be limited to managing crowd levels, booking time slots and maintaining attendance records.

A complete commercial gym platform may include features that are not required by a college gym. Its cost, suitability and compatibility with college rules will need to be checked.

## 3. Research Sources

### Source 1: Gymdesk – Gym Class Booking Software

**Website:** https://gymdesk.com/features/booking

**What I learned:**

Users can reserve gym sessions through an online booking schedule.

**Important Finding:**

Administrators can set session capacity and provide a waiting list when all available slots are booked.

**How it relates to my problem:**

This approach shows how advance booking and capacity limits can help manage the number of people visiting the gym.

However, booking records alone cannot show how many people are physically present. Actual occupancy would require check-in and check-out records.

### Source 2: MyGymDesk – Features

**Website:** https://mygymdesk.com/features

**What I learned:**

MyGymDesk provides features such as QR-code and biometric attendance, slot booking, class scheduling and capacity management.

**Important Finding:**

The platform connects session scheduling with attendance records. It also provides additional commercial features such as billing and member management.

**How it relates to my problem:**

It provides useful examples of digital booking and attendance systems. I will use these features as references while exploring whether a smaller and simpler system would be more suitable for a single college gym.

## 4. Initial Proposed Solution – GymFlow

I propose to build **GymFlow**, a simple campus gym slot-booking and crowd-management system.

The main goal is to help students and faculty members check gym availability before visiting and reduce overcrowding through better time-slot management.

### Proposed Features

**1. Slot Booking**

Users can view available gym time slots and book a suitable slot within the approved capacity.

**2. Live Occupancy Tracking**

The gym guard or another authorized person can record check-ins and check-outs to track the number of people currently inside the gym.

**3. Crowd Status Display**

The system can display the current occupancy using three colours:

- Green – Low occupancy.
- Yellow – Moderate occupancy.
- Red – Near capacity or full.

These limits will be decided with the gym administration.

**4. Digital Attendance**

The system can maintain basic digital attendance records for authorized users.

**5. Separate Time Slots**

Separate schedules for students, faculty or other groups may be introduced only if the gym administration confirms that they are necessary and permitted.

### Initial Scope

The first version of GymFlow will focus on three main features:

- Gym slot booking.
- Occupancy tracking.
- Digital attendance management.

The system will not collect personal fitness or medical information.

## 5. Questions to Validate During Fieldwork

I will ask the gym guard/attendant and other users the following questions to understand the actual problems and requirements:

1. What is the safe and practical maximum number of people who can use the gym at one time?
2. How is gym entry currently managed? Is attendance recorded anywhere?
3. When is the gym usually busiest? Do users have to wait for equipment or space?
4. Are there existing time slots or separate access rules for students and faculty?
5. Would online slot booking and a crowd-status display be useful? What improvements would users suggest?
6. Who would be allowed to manage bookings and attendance? What information can be recorded?

## 6. Fieldwork and Data-Collection Plan

I will personally visit the gym, observe its operations for at least **20 minutes** and speak with the gym guard/attendant or a regular gym user.

### Data I Will Collect

**1. Photographs**

With permission, I will take two timestamped photographs:
- One showing the overall gym environment.
- One showing the gym equipment or its arrangement.

**2. Observations**

I will collect at least **20 genuine observations**, such as:
- Timestamped counts of people present.
- Availability of gym equipment.
- Equipment being used or waiting users, where observable.
- Authorized attendance records, if access is permitted.

**3. Discussion**

I will speak with the guard/attendant or a regular user to understand:
- How gym entry and attendance are managed.
- When the gym is usually crowded.
- What problems users face.
- Whether a digital booking and crowd-management system would be useful.

**4. Privacy**

I will document how the information was collected and will not record identifiable personal details or take photographs of identifiable people without permission.

### Important Note

This document describes my initial understanding of the problem and my proposed solution. The fieldwork has not yet been completed.

After visiting the gym, I will update this research based on actual observations and conversations. If the findings reveal a different problem, existing process or more suitable solution, I will revise my proposal accordingly.

## 7. Expected Outcome

The research and fieldwork will help me understand whether gym overcrowding is a genuine problem at NIT Jamshedpur and how it currently affects students, faculty members and the gym guard/attendant.

Based on the collected observations and feedback, I will identify the actual requirements and refine GymFlow accordingly.

The final system will be designed around the gym's real needs, available resources and administrative rules rather than assumptions.
