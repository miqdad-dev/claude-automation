import pytest
from unittest.mock import patch
from worker import execute_task

@patch('time.sleep')
def test_execute_task(mock_sleep):
    execute_task('5')
    mock_sleep.assert_called_once_with(5)