from src.randomizer import randomizer
from src.lector_dir import lector_dir
from src.vlc_conector import vlc_conector
from src.find_xspf import find_xspf
import sys
# C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe
def app(xspf,VLC="C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"):
    vlc_conector(randomizer(lector_dir(find_xspf(xspf))),VLC)
    sys.exit()

if __name__ == "__main__":
    url_VLC=input("Introduce la ruta del VLC, si pulsas ENTER se entiende por que esta en program Files ")
    dir_xspf=input("Introduce el directorio donde se encuentran los xspf, si pulsas ENTER se entiende por que esta en este directorio ")
    if url_VLC  == "" and dir_xspf == "":
        app("../")
        
    elif url_VLC == "" :
        app(dir_xspf)
        
    elif dir_xspf == "":
        app("../", url_VLC)
    
    else:
        app(dir_xspf,url_VLC)