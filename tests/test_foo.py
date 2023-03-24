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
    # d = tmp_path / "sub"
    # d.mkdir()
    # p = d / "hello.txt"
    # p.write_text(CONTENT)
    # print(p)
    # assert p.read_text() == CONTENT
    # assert len(list(tmp_path.iterdir())) == 1


# class TickThread:
#     def __init__(self) -> None:
#         pass
#
#     def start(self) -> None:
#         print("********** Create Thread *********")
#         # self._stop_event = Lock()
#         # self._stop_event.acquire()
#         self._stop_event = Event()
#         self._thread = Thread(target=self._tick, args=(self._stop_event,))
#         self._thread.start()
#
#     def join(self) -> None:
#         self._stop_event.set()
#         print("*********** Join Thread **********")
#         self._thread.join()
#
#     @staticmethod
#     def _tick(stop_event) -> None:
#         global counter
#         while True:
#             print("Next")
#             counter += 1
#             if stop_event.wait(timeout=1):
#                 return
#
#     def __enter__(self) -> None:
#         self.start()
#
#     def __exit__(self, *_) -> None:
#         self.join()
#
#
# @pytest.mark.parametrize("n", range(128))
# def test_foo(n: int):
#     _ = n
#     global counter
#     global terminate
#     print("\n\n        Start Here")
#     check = 0
#     terminate = False
#     with TickThread():
#         sleep(2)
#         check = counter
#         counter = 0
#     assert check == 2
