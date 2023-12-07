from src.randomizer import randomizer
from src.lector_dir import lector_dir
from src.vlc_conector import vlc_conector
from src.find_xspf import find_xspf
import sys

def app():
    vlc_conector(randomizer(lector_dir(find_xspf())),"C:/Program Files (x86)/VideoLAN/VLC/vlc.exe")
    sys.exit()

if __name__ == "__main__":
    app()