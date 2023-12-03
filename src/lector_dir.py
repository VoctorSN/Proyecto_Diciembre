import xml.etree.ElementTree as ET
import sys

def lector_dir(files):
    locations=[]
    if len(files)==0:
        print("No hay fichero xspf")
        sys.exit()
    for file in files:
        elements = ET.parse(file).getroot().iter("{http://xspf.org/ns/0/}location")
        locations.extend([element.text for element in elements])
    return locations

if __name__ == "__main__":
    from find_xspf import find_xspf
    print(lector_dir(find_xspf()))
    # Si esta bien deberia dar las localizaciones de las canciones del fichero xspf