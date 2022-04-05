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
                CityName = element.find('nombre')
                CityRows = element.findall('fila')
                CityConvoys = element.findall('unidadMilitar')
                
                print(CityName)
                print(CityRows)
                print(CityConvoys)
                print('===========================================================\n') 
        

    except:
        print('No se cargaron los datos correctamente del piso')



if __name__ == '__main__':
    MiniDom(file)