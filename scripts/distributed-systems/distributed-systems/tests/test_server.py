import pytest
from unittest.mock import patch
from server import generate_workload

@patch('random.randint')
def test_generate_workload(mock_randint):
    mock_randint.return_value = 5
    assert generate_workload() == 5