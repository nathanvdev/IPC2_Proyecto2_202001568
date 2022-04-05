from xml.etree import ElementTree as ET

file = 'Docs/ArchivoPrueba.xml'

def ElementTree(file):
    try:
        tree = ET.parse(file)
        root = tree.getroot()
        
            
    except:
        print('No se cargaron los datos correctamente del piso "{}"'.format(element.attrib['nombre']))