"""Tests for the not gate."""
import pytest
from ivav.index_view import IndexView

STATE = [3, 1, 4, 1, 5, 9, 2, 6]
PARAMETERS = [
    [3, STATE.copy(), [1, 3, 1, 4, 9, 5, 6, 2], 0],
    [3, STATE.copy(), [4, 1, 3, 1, 2, 6, 5, 9], 1],
    [3, STATE.copy(), [5, 9, 2, 6, 3, 1, 4, 1], 2],
]


@pytest.mark.parametrize("n, state_vector, expected_state_vector, index",
                         PARAMETERS)
def test_not_gate(n, state_vector, expected_state_vector, index):
    index_view = IndexView(n, state_vector)
    index_view.x(index)
    assert all(index_view.state_vector == expected_state_vector)
