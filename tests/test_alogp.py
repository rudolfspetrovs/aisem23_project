import pytest
import numpy as np
from src.project_web.molecules_properties.alogp import get_data


def test_empty_data():
    assert get_data([]) == {}


@pytest.fixture
def sample_raw_data():
    return [
        {
            "molecule_properties": {"alogp": 1.0}
        },
        {
            "molecule_properties": {"alogp": None}
        },
        {
            "molecule_properties": {"alogp": 2.0}
        }
    ]


def test_get_data(sample_raw_data):
    expected_output = {
        "component": "aLogP",
        "data": [1.0, 2.0],
        "mean": np.mean([1.0, 2.0]),
        "std": np.std([1.0, 2.0], ddof=1),
        "min_value": np.min([1.0, 2.0]),
        "max_value": np.max([1.0, 2.0]),
    }

    assert get_data(sample_raw_data) == expected_output
