from cgi import print_directory
from xml.etree import ElementTree as ET

file = 'Docs/ArchivoPrueba.xml'

def MiniDom(file):
    try:
        tree = ET.parse(file)
        root = tree.getroot()
        for element in root:
            ciudades = element.findall('ciudad')
            for ciudad in ciudades:
                CityName = ciudad.find('nombre')
                CityRows = ciudad.findall('fila')
                CityConvoys = ciudad.findall('unidadMilitar')
                
                print(CityName.text)
                for Row in CityRows:
                    print(Row.attrib['numero'], Row.text)
                for Convoy in CityConvoys:
                    print(Convoy.text)
                print('===========================================================\n') 
        

    except:
        print('No se cargaron los datos correctamente del piso')



if __name__ == '__main__':
    MiniDom(file)