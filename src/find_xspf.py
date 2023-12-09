import os

def find_xspf(dir_xspf="../"):
    if dir_xspf in ("../",""):
        return [file for file in os.listdir() if file.endswith(".xspf")]
    try:
        directorio=os.listdir(dir_xspf.replace("\\","/"))
        return [dir_xspf.replace("\\","/")+"/"+file for file in directorio if file.endswith(".xspf") and os.path.exists(dir_xspf+"/"+file)]
    except FileNotFoundError:
        print("Esta ruta no existe")
        return None
    except NotADirectoryError:
        print("Esto es un archivo no un directorio")
        return None

if __name__ == "__main__":
    print(find_xspf())