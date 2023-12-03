import xml.etree.ElementTree as ET

def lector_dir(files):
    locations=[]
    if len(files)==0:
        return "No hay fichero xspf"
    for file in files:
        for element in list(ET.parse(file).getroot().iter("{http://xspf.org/ns/0/}location")):
            locations.append(element.text)
    return locations

if __name__ == "__main__":
    from find_xspf import find_xspf
    print(lector_dir(find_xspf()))
    # Si esta bien deberia dar las localizaciones de las canciones del fichero xspf