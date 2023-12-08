from src.randomizer import randomizer
import pytest

@pytest.mark.randomizer
def test_len():
    assert len(randomizer([1,23,42,13,135,3,65,3,423423,423423]))==10

@pytest.mark.randomizer_Error
def test_randomizer_error():
    assert randomizer([])==None

@pytest.mark.randomizer
def test_no_values_lost():
    for value in randomizer([1,23,1432,53123,135324,2,"adaw","dawda","a32"]):
        if value not in [1,23,1432,53123,135324,2,"adaw","dawda","a32"]:
            assert False