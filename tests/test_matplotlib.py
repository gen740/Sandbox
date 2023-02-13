import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.style as mplstyle
import pytest

mpl.use("QtAgg")

mplstyle.use("fast")


@pytest.mark.parametrize("n", [i for i in range(1000)])
def test(n: int):
    plt.figure()
    plt.close()
    _ = n
