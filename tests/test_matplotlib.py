import matplotlib.pyplot as plt
import matplotlib.style as mplstyle
import pytest

mplstyle.use("fast")


@pytest.mark.parametrize("n", [i for i in range(1000)])
def test(n: int):
    plt.figure()
    plt.close()
    _ = n
