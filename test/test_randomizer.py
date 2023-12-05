from src.randomizer import randomizer
def test_len():
    assert len(randomizer([1,23,42,13,135,3,65,3,423423,423423]))==10

def test_randomizer_error():
    assert randomizer([])==None

def test_no_values_lost():
    for value in randomizer([1,23,1432,53123,135324,2,"adaw","dawda","a32"]):
        if value not in [1,23,1432,53123,135324,2,"adaw","dawda","a32"]:
            assert False