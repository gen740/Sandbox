import matplotlib.pyplot as plt
import pytest


@pytest.mark.parametrize("n", [i for i in range(2500)])
def test(n: int):
    plt.figure()
    plt.close()
    _ = n
