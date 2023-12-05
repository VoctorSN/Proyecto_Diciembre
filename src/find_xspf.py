import os

def find_xspf():
    dir_xspf=input("Introduce la ruta de la carpeta de los xspf, si esta carpetas es la carpeta Proyecto_Diciembre simplemente pulsa ENTER ")
    if dir_xspf=="":
        return [file for file in os.listdir() if file.endswith(".xspf")]
    files=[dir_xspf+"/"+file for file in os.listdir(dir_xspf) if file.endswith(".xspf") and os.path.exists(dir_xspf+"/"+file)]
    return files

if __name__ == "__main__":
    print(find_xspf())
    