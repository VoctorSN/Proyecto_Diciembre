from src.find_xspf import find_xspf
def test_find_one():
    assert "canciones.xspf" in find_xspf()

def test_find_all_xspf():
    assert "canciones_profe.xspf" in find_xspf() and "canciones.xspf" in find_xspf()