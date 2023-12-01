from src.lector_dir import lector_dir
from src.find_xspf import find_xspf


def test_archivos():
    assert "file:///C:/Users/victo/Escritorio/Clase/PR/Proyecto_Diciembre/biblioteca/King_Kunta.mp3" in lector_dir(find_xspf())