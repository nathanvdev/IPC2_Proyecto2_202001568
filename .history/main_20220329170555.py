from xml.etree import ElementTree as ET

file = 'Docs/ArchivoPrueba.xml'

def MiniDom(file):
    try:
        tree = ET.parse(file)
        root = tree.getroot()
        for element in root:
            print(element.find('ciudad'))
        

    except:
        print('No se cargaron los datos correctamente del piso')



if __name__ == '__main__':
    MiniDom(file)