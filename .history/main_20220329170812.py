from cgi import print_directory
from xml.etree import ElementTree as ET

file = 'Docs/ArchivoPrueba.xml'

def MiniDom(file):
    try:
        tree = ET.parse(file)
        root = tree.getroot()
        for element in root:
            ciudades = element.findall('ciudad')
            for e in ciudades:
                for filas in e:
                    print(filas)
                print('*****')
        

    except:
        print('No se cargaron los datos correctamente del piso')



if __name__ == '__main__':
    MiniDom(file)