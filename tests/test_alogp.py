import pytest
from src.project_web.molecules_properties.alogp import get_data


def test_empty_data():
    assert get_data([]) == {}
