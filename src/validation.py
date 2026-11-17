"""Validation for historical GymFlow observations."""

from __future__ import annotations

from dataclasses import dataclass, field

import pandas as pd


REQUIRED_COLUMNS = (
    "timestamp",
    "people_present",
    "equipment_in_use",
    "equipment_total",
    "waiting_people",
)
NUMERIC_COLUMNS = REQUIRED_COLUMNS[1:]


@dataclass
class ValidationReport:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        return not self.errors


def validate_observations(data: pd.DataFrame, capacity: int) -> ValidationReport:
    """Validate columns and values without changing the uploaded DataFrame."""
    report = ValidationReport()
    missing = [column for column in REQUIRED_COLUMNS if column not in data.columns]
    if missing:
        report.errors.append(f"Missing required columns: {', '.join(missing)}.")
        return report
    if data.empty:
        report.errors.append("The dataset contains no observation rows.")
        return report
    if capacity <= 0:
        report.errors.append("Capacity must be greater than zero.")
        return report

    blank_timestamp_rows = data.index[data["timestamp"].isna()].tolist()
    if blank_timestamp_rows:
        report.errors.append(f"Missing timestamp in row(s): {_rows(blank_timestamp_rows)}.")
    parsed_times = pd.to_datetime(data["timestamp"], errors="coerce")
    invalid_time_rows = data.index[parsed_times.isna() & data["timestamp"].notna()].tolist()
    if invalid_time_rows:
        report.errors.append(f"Invalid timestamp in row(s): {_rows(invalid_time_rows)}.")

    numeric_data = data.loc[:, NUMERIC_COLUMNS].apply(pd.to_numeric, errors="coerce")
    for column in NUMERIC_COLUMNS:
        invalid = data.index[numeric_data[column].isna()].tolist()
        if invalid:
            report.errors.append(f"{column} must be numeric in row(s): {_rows(invalid)}.")
            continue
        negative = data.index[numeric_data[column] < 0].tolist()
        if negative:
            report.errors.append(f"{column} cannot be negative in row(s): {_rows(negative)}.")

    if numeric_data["people_present"].notna().any():
        over_capacity = data.index[numeric_data["people_present"] > capacity].tolist()
        if over_capacity:
            report.errors.append(
                f"people_present exceeds the current capacity ({capacity}) in row(s): {_rows(over_capacity)}."
            )
    if numeric_data[["equipment_in_use", "equipment_total"]].notna().all(axis=None):
        over_equipment = data.index[numeric_data["equipment_in_use"] > numeric_data["equipment_total"]].tolist()
        if over_equipment:
            report.errors.append(f"equipment_in_use exceeds equipment_total in row(s): {_rows(over_equipment)}.")
    return report


def _rows(indexes: list[object]) -> str:
    """Present zero-based DataFrame indexes as familiar spreadsheet row numbers."""
    return ", ".join(str(int(index) + 2) for index in indexes)
