import datetime
import random
import time
import sys

import pytest
from tqdm import tqdm


@pytest.mark.parametrize("n", [i for i in range(100)])
def test_tqdm(n: int, capsys: pytest.CaptureFixture):
    _ = n

    tqdm_main()

    _, err = capsys.readouterr()
    assert "100%" in err


def tqdm_main():
    timeout = 1
    total = tqdm.format_interval(100)
    fmt = "{desc} {percentage:3.0f}%|{bar}| {elapsed}/" + total
    progress_bar = tqdm(total=timeout, bar_format=fmt)
    time_start = datetime.datetime.now()
    last_elapsed_seconds = 0.0

    while True:
        elapsed_seconds = (datetime.datetime.now() - time_start).total_seconds()
        time_diff = elapsed_seconds - last_elapsed_seconds

        if elapsed_seconds > timeout:
            # Clip elapsed time to avoid tqdm warnings.
            time_diff -= elapsed_seconds - timeout

        progress_bar.update(time_diff)
        print("*" * 1000, file=sys.stderr)
        last_elapsed_seconds = elapsed_seconds

        if elapsed_seconds > timeout:
            break

        time.sleep(random.random() * 0.1)


if __name__ == "__main__":
    tqdm_main()
