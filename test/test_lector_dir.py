from src.lector_dir import lector_dir
from src.find_xspf import find_xspf
import pytest

@pytest.mark.lector_dir_Error
def test_0_files():
    assert lector_dir([]) is None

@pytest.mark.lector_dir_Error
def test_files_is_none():
    assert lector_dir(find_xspf("patata/files.xspf")) is None

@pytest.mark.lector_dir_not_in
def test_prueba_mala():
    assert "/canciones/pruebamala.txt" not in lector_dir(find_xspf())

@pytest.mark.lector_dir_not_in
def test_menos_de_8_con_espacios():
    assert r"%20%20%20%20" not in lector_dir(find_xspf())

@pytest.mark.lector_dir_not_in
def test_menos_de_8():
    assert "nollega" not in lector_dir(find_xspf())
