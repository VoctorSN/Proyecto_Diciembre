from src.lector_dir import lector_dir


def test_archivos():
    assert "file:///D:/P/python/Proyecto_diciembre/songs/A_Virtual_Friend_-_Clair_Obscur.mp3" in lector_dir()