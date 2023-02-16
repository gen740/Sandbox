import os

import matplotlib as mpl
import matplotlib.pyplot as plt
import pytest


@pytest.mark.qtagg
def test_environment():
    assert os.environ.get("MPLBACKEND") == "QtAgg"


@pytest.mark.qtagg
def test_check_backend():
    assert mpl.get_backend() == "QtAgg"


@pytest.mark.parametrize("n", [i for i in range(2500)])
def test(n: int):
    plt.figure()
    plt.close()
    _ = n
