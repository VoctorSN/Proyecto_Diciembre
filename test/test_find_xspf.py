from src.find_xspf import find_xspf
def test_find_one():
    assert "canciones_mias.xspf" in find_xspf()

def test_find_in_canciones_xspf():
    assert r"D:\P\python\Proyecto_Diciembre\canciones_xspf\canciones_mias.xspf" in find_xspf()

def test_find_all_xspf():
    assert "canciones_profe.xspf" in find_xspf() and "canciones_mias.xspf" in find_xspf()

def test_with_location():
    assert find_xspf() is None