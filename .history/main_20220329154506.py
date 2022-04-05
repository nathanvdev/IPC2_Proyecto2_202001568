

file = 'Docs/ArchivoPrueba.xml'

def ElementTree(file):
    try:
         tree = ET.parse(file)
        root = tree.getroot()
    except:
        pass