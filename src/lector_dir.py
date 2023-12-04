import xml.etree.ElementTree as ET
import os.path

def lector_dir(files):
    locations=[]
    files_not_located=0
    files_located=0
    if len(files)==0:
        print("No hay fichero xspf")
        return None
    for file in files:
        elements = ET.parse(file).getroot().iter("{http://xspf.org/ns/0/}location")
        for element in elements:
            if len(element.text)<=8:
                files_not_located+=1
            elif os.path.exists(element.text[8:]):
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