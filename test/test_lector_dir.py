from src.lector_dir import lector_dir
from src.find_xspf import find_xspf

def test_0_files():
    assert lector_dir([])==None
def test_archivos_cancionesxspf():
    assert "file:///D:/P/python/Proyecto_Diciembre/songs/Boukmanflow_-_Does_she_not.mp3" in lector_dir(find_xspf())
def test_archivos_profexspf():
     assert "file:///D:/P/python/Proyecto_Diciembre/biblioteca/against%20the%20moon.mp3" in lector_dir(find_xspf())
def test_prueba_mala():
    assert "file:///C:/Users/victo/Escritorio/Clase/PR/Proyecto_Diciembre/songs/pruebamala.txt" not in lector_dir(find_xspf())
def test_en_casa():
    assert "file:///C:/Users/victo/Escritorio/Clase/PR/Proyecto_Diciembre/songs/Mejor%20cancion.mp3" not in lector_dir(find_xspf())