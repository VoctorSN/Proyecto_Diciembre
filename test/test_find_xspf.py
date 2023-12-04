from src.find_xspf import find_xspf
def test_find_one():
    assert "canciones_mias.xspf" in find_xspf()

def test_find_all_xspf():
    assert "canciones_profe.xspf" in find_xspf() and "canciones_mias.xspf" in find_xspf()

def test_with_location():
    assert "canciones_mias.xspf" in find_xspf("C:/Users/a23victorsn/Desktop")