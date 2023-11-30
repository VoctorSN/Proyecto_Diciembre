import os
def lector_dir():
    archivos=os.listdir("songs")
    archivos_mp3=[]
    for archivo in archivos:
        if archivo.endswith(".mp3"):
            archivos_mp3.append(archivo)
        else:
            continue
    return archivos_mp3