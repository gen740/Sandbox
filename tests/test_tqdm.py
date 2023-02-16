import pytest
from tqdm import tqdm


@pytest.mark.parametrize("n", [i for i in range(1000)])
def test_tqdm(n: int, capsys: pytest.CaptureFixture):
    _ = n
    for _ in tqdm(range(1000)):
        pass

    _, err = capsys.readouterr()

    assert "100%" in err
