# On Windows, temporary file shold delete "after" storage was deleted
# NamedTemporaryFilePool ensures tempfile delete after tests.

import pytest

from foo.tempfile_pool import NamedTemporaryFilePool


@pytest.mark.parametrize("n", range(10))
def test_foo(n: int):
    with pytest.raises(ValueError):
        int("aoe")

    with NamedTemporaryFilePool(suffix="{SCHEMA_VERSION}") as tf:
        print(tf.name)
