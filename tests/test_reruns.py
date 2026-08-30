import pytest
import random

@pytest.mark.flaky(reruns=5)
def test_reruns():
    assert random.choice([False, True])

    

