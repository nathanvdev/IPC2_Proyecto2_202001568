from xml.etree import ElementTree as ET

file = 'Docs/ArchivoPrueba.xml'

def MiniDom(file):
    try:
        tree = ET.parse(file)
        root = tree.getroot()
        ciudades = root.getele
        for element in root:
            for subelement in element:
                print(subelement)

    except:
        print('No se cargaron los datos correctamente del piso')



if __name__ == '__main__':
    MiniDom(file)