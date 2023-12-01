import subprocess

def vlc_conector(urls_random):
    try:
        comando=["C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"] + urls_random
        subprocess.run(comando, check=False)
    except FileNotFoundError:
        try:
            comando=["C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"] + urls_random
            subprocess.run(comando, check=False)
        except FileNotFoundError:
            return "No se encuentra el vlc.exe"


if __name__ == "__main__":
    vlc_conector(['file:///D:/P/python/Proyecto_diciembre/songs/A_Virtual_Friend_-_Clair_Obscur.mp3', 'file:///D:/P/python/Proyecto_diciembre/songs/Boukmanflow_-_Does_she_not.mp3', 'file:///D:/P/python/Proyecto_diciembre/songs/Mejor%20cancion.mp3', 'file:///D:/P/python/Proyecto_diciembre/songs/PUETO_PA_LO_MIO_RECORDS_-_YO_NO_ENTIENDO_-_PUETO_PA_LO_MIO_RECORDS_Presenta_-_-_NEYCOM.mp3'])