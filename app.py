from src.randomizer import randomizer
from src.lector_dir import lector_dir
from src.vlc_conector import vlc_conector

def app():
    vlc_conector(randomizer(lector_dir()))

if __name__ == "__main__":
    app()