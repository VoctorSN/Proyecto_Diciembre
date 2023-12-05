import xml.etree.ElementTree as ET
import os.path

def lector_dir(files):
    locations=[]
    files_not_located=0
    files_located=0
    if len(files)==0:
        print("No hay ficheros xspf, prueba a poner la ruta de las canciones como argumento")
        return None
    try:
        for file in files:
            for element in ET.parse(file).getroot().iter("{http://xspf.org/ns/0/}location"):
                if len(element.text.replace("%20"," "))<=8:
                    files_not_located+=1
                elif os.path.exists(element.text.replace("%20"," ").replace("file:///","")):
                    locations.append(element.text)
                    files_located+=1
                else:
                    files_not_located+=1
        print("Existian ",files_located+files_not_located," enlaces, de los cuales ",files_located," se han detectado y ",files_not_located," no se han detectado en tu dispositivo")
        return locations
    except FileNotFoundError:
        print("No hay ficheros xspf, prueba a poner la ruta de las canciones como argumento")
        return find_xspf(r"D:\P\python\Proyecto_Diciembre\prueba")

if __name__ == "__main__":
    from find_xspf import find_xspf
    print(lector_dir(find_xspf()))
    # Si esta bien deberia dar las localizaciones de las canciones del fichero xspf