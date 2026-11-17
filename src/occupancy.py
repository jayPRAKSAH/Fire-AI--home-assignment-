"""Pure calculations used by the GymFlow dashboard."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


@dataclass(frozen=True)
class CrowdStatus:
    """A human-readable occupancy state and its display colour."""

    label: str
    colour: str
    message: str


def occupancy_percentage(people_present: int | float, capacity: int | float) -> float:
    """Return occupancy as a percentage, rejecting a non-positive capacity."""
    if capacity <= 0:
        raise ValueError("Capacity must be greater than zero.")
    return round((float(people_present) / float(capacity)) * 100, 1)


def available_spaces(people_present: int | float, capacity: int | float) -> int:
    """Return remaining physical spaces (never a negative number)."""
    if capacity < 0:
        raise ValueError("Capacity cannot be negative.")
    return max(0, int(capacity - people_present))


def crowd_status(
    people_present: int | float,
    capacity: int | float,
    moderate_threshold: float = 50,
    high_threshold: float = 85,
) -> CrowdStatus:
    """Classify occupancy with configurable yellow/red thresholds."""
    if not 0 <= moderate_threshold < high_threshold <= 100:
        raise ValueError("Thresholds must satisfy 0 <= moderate < high <= 100.")

    percentage = occupancy_percentage(people_present, capacity)
    if percentage < moderate_threshold:
        return CrowdStatus("Available", "green", "Plenty of room to work out.")
    if percentage < high_threshold:
        return CrowdStatus("Moderate", "yellow", "The gym is getting busy.")
    return CrowdStatus("Busy", "red", "Consider visiting at a quieter time.")


def historical_summary(data: pd.DataFrame, capacity: int) -> dict[str, object]:
    """Calculate concise historical metrics from a validated observation set."""
    if data.empty:
        raise ValueError("No observations are available for analysis.")

    highest = data.loc[data["people_present"].idxmax()]
    lowest = data.loc[data["people_present"].idxmin()]
    return {
        "observation_count": len(data),
        "average_people": round(float(data["people_present"].mean()), 1),
        "average_occupancy": round(float(data["people_present"].mean() / capacity * 100), 1),
        "busiest_timestamp": str(highest["timestamp"]),
        "busiest_people": int(highest["people_present"]),
        "quietest_timestamp": str(lowest["timestamp"]),
        "quietest_people": int(lowest["people_present"]),
    }
