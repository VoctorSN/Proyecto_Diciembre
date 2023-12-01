from src.randomizer import randomizer
from src.lector_dir import lector_dir
from src.vlc_conector import vlc_conector
from src.find_xspf import find_xspf

def app():
    vlc_conector(randomizer(lector_dir(find_xspf())))

if __name__ == "__main__":
    app()