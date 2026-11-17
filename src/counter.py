"""File-backed manual occupancy counter and audit log."""

from __future__ import annotations

import csv
import json
import os
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_STATE = {"people_present": 0, "capacity": 25, "updated_at": None}


def load_state(state_path: Path) -> dict[str, int | str | None]:
    """Return persisted state, or a safe default before first use."""
    if not state_path.exists():
        return DEFAULT_STATE.copy()
    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
        people = int(state["people_present"])
        capacity = int(state["capacity"])
        if not 0 <= people <= capacity or capacity <= 0:
            raise ValueError
        return {"people_present": people, "capacity": capacity, "updated_at": state.get("updated_at")}
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
        raise ValueError("The saved counter state is invalid. Delete the state file and try again.") from error


def update_count(state_path: Path, log_path: Path, change: int) -> dict[str, int | str | None]:
    """Apply a single entry (+1) or exit (-1), then save an auditable update."""
    if change not in {-1, 1}:
        raise ValueError("Counter changes must be +1 or -1.")
    state = load_state(state_path)
    next_count = int(state["people_present"]) + change
    if next_count < 0:
        raise ValueError("The gym is already empty.")
    if next_count > int(state["capacity"]):
        raise ValueError("The gym is already at full capacity.")

    timestamp = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    updated = {**state, "people_present": next_count, "updated_at": timestamp}
    _save_state(state_path, updated)
    _append_log(log_path, timestamp, "entry" if change > 0 else "exit", next_count)
    return updated


def set_capacity(state_path: Path, capacity: int) -> dict[str, int | str | None]:
    """Persist a confirmed capacity while preserving the current count."""
    state = load_state(state_path)
    if capacity <= 0:
        raise ValueError("Capacity must be greater than zero.")
    if capacity < int(state["people_present"]):
        raise ValueError("Capacity cannot be lower than the current number of people inside.")
    updated = {**state, "capacity": int(capacity)}
    _save_state(state_path, updated)
    return updated


def _save_state(path: Path, state: dict[str, int | str | None]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = path.with_suffix(".tmp")
    temporary_path.write_text(json.dumps(state, indent=2), encoding="utf-8")
    os.replace(temporary_path, path)


def _append_log(path: Path, timestamp: str, action: str, count_after: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    needs_header = not path.exists()
    with path.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["timestamp", "action", "count_after"])
        if needs_header:
            writer.writeheader()
        writer.writerow({"timestamp": timestamp, "action": action, "count_after": count_after})
