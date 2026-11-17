from pathlib import Path

import pandas as pd
import pytest

from src.counter import load_state, set_capacity, update_count
from src.occupancy import available_spaces, crowd_status, occupancy_percentage
from src.validation import validate_observations


def test_occupancy_calculations_and_statuses():
    assert occupancy_percentage(15, 25) == 60.0
    assert available_spaces(15, 25) == 10
    assert crowd_status(5, 25).label == "Available"
    assert crowd_status(15, 25).label == "Moderate"
    assert crowd_status(23, 25).label == "Busy"


def test_validation_reports_invalid_values():
    observations = pd.DataFrame(
        {"timestamp": ["not-a-time"], "people_present": [-1], "equipment_in_use": [5], "equipment_total": [4], "waiting_people": [0]}
    )
    report = validate_observations(observations, 25)
    assert not report.is_valid
    assert any("Invalid timestamp" in error for error in report.errors)
    assert any("cannot be negative" in error for error in report.errors)
    assert any("exceeds equipment_total" in error for error in report.errors)


def test_counter_persists_and_enforces_bounds(tmp_path: Path):
    state_path, log_path = tmp_path / "state.json", tmp_path / "log.csv"
    set_capacity(state_path, 2)
    assert update_count(state_path, log_path, 1)["people_present"] == 1
    assert update_count(state_path, log_path, 1)["people_present"] == 2
    with pytest.raises(ValueError, match="full"):
        update_count(state_path, log_path, 1)
    assert update_count(state_path, log_path, -1)["people_present"] == 1
    assert load_state(state_path)["capacity"] == 2
