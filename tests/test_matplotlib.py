import matplotlib.pyplot as plt
import pytest


@pytest.mark.parametrize("n", [i for i in range(1000)])
def test(n: int):
    plt.figure()
    plt.close()
    _ = n
