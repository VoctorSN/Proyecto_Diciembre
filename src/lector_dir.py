import xml.etree.ElementTree as ET
def lector_dir():
    tree = ET.parse('canciones.xspf')
    root=tree.getroot()
    for child in root:
        if child.tag.endswith("trackList"):
            for track in child:
                if track.tag.endswith("track"):
                    for element in track:
                        if element.tag.endswith("title"):
                            print(element.text)
    
lector_dir()