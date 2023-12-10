from src.find_xspf import find_xspf
import pytest

@pytest.mark.find_xspf
def test_find_one():
    assert "canciones.xspf" in find_xspf()

@pytest.mark.find_xspf
def test_find_in_canciones_xspf():
    assert "canciones_xspf/canciones.xspf" in find_xspf("canciones_xspf")

@pytest.mark.find_xspf
def test_find_all_xspf():
    assert "canciones_profe.xspf" in find_xspf() and "canciones.xspf" in find_xspf()

@pytest.mark.find_xspf_Error
def test_NotAFileError():
    assert find_xspf("patata/files.xspf") is None
    
@pytest.mark.find_xspf_Error
def test_not_a_dir():
    assert find_xspf("C:/Program Files (x86)/VideoLAN/VLC/vlc.exe")==None
    