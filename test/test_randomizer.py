from src.randomizer import randomizer
def test_len():
    assert len(randomizer([1,23,42,13,135,3,65,3,423423,423423]))==10
    assert randomizer([])==None

def test_diff_order():
    assert randomizer([1,23,1432,53123,135324,2,"adaw","dawda","a32"])!=[1,23,1432,53123,135324,2,"adaw","dawda","a32"]