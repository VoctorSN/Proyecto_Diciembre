import xml.etree.ElementTree as ET
import os.path

def lector_dir(files):
    traductor={"%20":" ","%26":"&","%28":"(","%29":")","%2C":",","%40":"@","%2":":","%5D":"]","%5B":"[","file:///":""}
    locations=[]
    files_not_located=0
    files_located=0
    if files is None:
        return None
    if len(files)==0:
        print("No hay ficheros xspf, prueba a poner la ruta de las canciones como argumento")
        return None
    for file in files:
        for element in ET.parse(file).getroot().iter("{http://xspf.org/ns/0/}location"):
            ruta=element.text
            for caracter,traduccion in traductor.items():
                ruta=ruta.replace(caracter,traduccion)
            if os.path.exists(ruta):
                locations.append(element.text)
                files_located+=1
            else:
                files_not_located+=1
    print("Existian ",files_located+files_not_located," enlaces, de los cuales ",files_located," se han detectado y ",files_not_located," no se han detectado en tu dispositivo")
    return locations

if __name__ == "__main__":
    from find_xspf import find_xspf
    print(lector_dir(find_xspf()))
    # Si esta bien deberia dar las localizaciones de las canciones del fichero xspf