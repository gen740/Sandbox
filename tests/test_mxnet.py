from typing import List, Self

import pytest


class TempFile:
    counter = 0

    def __call__(self) -> Self:
        self.counter = TempFile.counter
        TempFile.counter += 1
        return self

    def __str__(self) -> str:
        return str(self.counter)

    def __del__(self):
        print(f"deleted {self.counter}")


class TemplateFileRAII:
    tempfile_pool: List[TempFile] = []

    def __call__(self):
        temp = TempFile()
        TemplateFileRAII.tempfile_pool.append(temp)
        return temp


def test_description():
    print(pytest.mark.foo)
