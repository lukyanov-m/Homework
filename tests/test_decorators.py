import os

import pytest

from src.decorators import log


def test_log_error_to_console(capsys):
    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError" in captured.out
    assert "Inputs: (1, 0)" in captured.out


def read_log(filename):
    with open(filename, "r") as f:
        return f.read()


def test_log_success_to_file(tmp_path):
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def add(a, b):
        return a + b

    result = add(2, 3)

    assert result == 5
    assert os.path.exists(log_file)
    log_content = read_log(log_file)
    assert "add Ok. Inputs: (2, 3)" in log_content
