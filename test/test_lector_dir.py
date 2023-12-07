from src.lector_dir import lector_dir
from src.find_xspf import find_xspf

def test_0_files():
    assert lector_dir([]) is None

def test_files_is_none():
    assert lector_dir(find_xspf("patata/files.xspf")) is None
    
def test_archivos_cancionesxspf():
    assert "file:///C:/Users/victo/Escritorio/Clase/PR/Proyecto_Diciembre/songs/Boukmanflow_-_Does_she_not.mp3" in lector_dir(find_xspf())
            
def test_archivos_profexspf():
     assert "file:///C:/Users/victo/Escritorio/Clase/PR/Proyecto_Diciembre/biblioteca/against%20the%20moon.mp3" in lector_dir(find_xspf())
             
def test_prueba_mala():
    assert "file:///C:/Users/victo/Escritorio/Clase/PR/Proyecto_Diciembre/songs/pruebamala.txt" not in lector_dir(find_xspf())
def test_menos_de_8_con_espacios():
    assert r"%20%20%20%20" not in lector_dir(find_xspf())
def test_menos_de_8():
    assert "nollega" not in lector_dir(find_xspf())

def test_en_casa():
    assert "file:///C:/Users/victo/Escritorio/Clase/PR/Proyecto_Diciembre/songs/Mejor%20cancion.mp3" in lector_dir(find_xspf())