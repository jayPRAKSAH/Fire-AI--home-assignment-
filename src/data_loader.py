"""CSV/XLSX loading and preparation for GymFlow."""

from __future__ import annotations

from pathlib import Path
from typing import BinaryIO

import pandas as pd

from src.validation import NUMERIC_COLUMNS


class DataLoadError(ValueError):
    """Raised when an observation file cannot be read."""


def load_observations(uploaded_file: BinaryIO | Path | str) -> pd.DataFrame:
    """Load a CSV or XLSX file and return a clean, predictable table."""
    name = getattr(uploaded_file, "name", str(uploaded_file)).lower()
    try:
        if name.endswith(".csv"):
            data = pd.read_csv(uploaded_file)
        elif name.endswith(".xlsx"):
            data = pd.read_excel(uploaded_file)
        else:
            raise DataLoadError("Unsupported file type. Upload a CSV or XLSX file.")
    except DataLoadError:
        raise
    except Exception as error:
        raise DataLoadError(f"Unable to read the uploaded file: {error}") from error

    data.columns = [str(column).strip().lower().replace(" ", "_") for column in data.columns]
    for column in NUMERIC_COLUMNS:
        if column in data.columns:
            data[column] = pd.to_numeric(data[column], errors="coerce")
    return data


def load_sample_data(path: Path) -> pd.DataFrame:
    """Load the bundled development-only sample data."""
    return load_observations(path)
