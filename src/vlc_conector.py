import subprocess
import sys

def vlc_conector(urls_random):
    possible_urls=["C:\\Program Filess\\VideoLAN\\VLC\\vlc.exe","C:\\Program Filess (x86)\\VideoLAN\\VLC\\vlc.exe"]
    for tries in possible_urls:
        executed=False
        try:
            comando=[tries] + urls_random
            subprocess.run(comando, check=False)
            executed=True
        except FileNotFoundError:
            pass
    if not executed:
        print("No se encuentra el vlc.exe")
        sys.exit()


if __name__ == "__main__":
    from find_xspf import find_xspf
    from lector_dir import lector_dir
    from randomizer import randomizer
    # Para que funcione tendria que reproducir las canciones ya desordenadas
    vlc_conector(randomizer(lector_dir(find_xspf())))