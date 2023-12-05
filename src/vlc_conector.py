import subprocess

def vlc_conector(urls_random):
    url_user=input(r"Introduce la ruta de tu VLC separado con doble '\\' y sin comillas, si pulsas enter se entiende que esta en Program Files ")
    if not urls_random:
        return None
    try:
        if url_user=="":
            comando=["C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"] + urls_random
            subprocess.run(comando, check=False)
            return True
        comando=[url_user] + urls_random
        subprocess.run(comando, check=False)
        return True
    except FileNotFoundError:
        print("No se encuentra el vlc.exe")
        return None


if __name__ == "__main__":
    from find_xspf import find_xspf
    from lector_dir import lector_dir
    from randomizer import randomizer
    # Para que funcione tendria que reproducir las canciones ya desordenadas
    vlc_conector(randomizer(lector_dir(find_xspf())))