import pytest
from generate_data import generate_data


def test_generate_single_data():
    excepted_result = generate_data(1)
    assert len(excepted_result) == 1
    assert excepted_result[0] is not None
