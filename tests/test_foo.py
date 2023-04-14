import tempfile
from pathlib import Path, PosixPath
from threading import Event, Lock, Thread
from time import sleep

import pytest

counter = 0

# content of test_tmp_path.py
CONTENT = "content"


def test_foo(tmp_path):
    assert type(tmp_path).__name__ == "PosixPath"
