from src.lector_dir import lector_dir


def test_archivos():
    assert "Mejor cancion.mp3" in lector_dir()

def test_solo_mp3():
    assert "Mejor cancion.mp3" in lector_dir()
    assert "pruebamala" not in lector_dir()