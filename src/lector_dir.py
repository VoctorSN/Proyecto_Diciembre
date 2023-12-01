import xml.etree.ElementTree as ET
def lector_dir():
    return [element.text for element in 
            list(ET.parse('canciones.xspf').getroot().iter("{http://xspf.org/ns/0/}location"))]

if __name__ == "__main__":
    print(lector_dir())
    # Si esta bien deberia dar las localizaciones de las canciones del fichero xspf