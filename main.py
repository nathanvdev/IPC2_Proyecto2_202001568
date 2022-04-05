from traceback import print_tb
from typing import final
from xml.etree import ElementTree as ET
from SparceMatrix import SparceMatrix
from Cities import ListCities, NodeCity

file = 'Docs/ArchivoPrueba.xml'

CitiesList = ListCities()

def ElementTree(file):
    try:
        tree = ET.parse(file)
        root = tree.getroot()
        for element in root:
            cities = element.findall('ciudad')
            for City in cities:
                CityName = City.find('nombre')
                CityRows = City.findall('fila')
                CityConvoys = City.findall('unidadMilitar')
                
                print(CityName.text, CityName.attrib['filas'], CityName.attrib['columnas'])
                NewCity = NodeCity(CityName.text, CityName.attrib['filas'], CityName.attrib['columnas'])
                
                for Row in CityRows:
                    patron = Row.text.replace('"','')
                    PosX = 0
                    PosY = int(Row.attrib['numero'])
                    PosY = PosY -1
                    for character in patron:
                        if character != '*':
                            NewCity.Pattern.Insert(PosX, PosY, character)
                        PosX += 1    
                            
                for Convoy in CityConvoys:
                    print(Convoy.text)
                    PosX = int(Convoy.attrib['columna'])
                    PosY = int(Convoy.attrib['fila'])
                    finded = NewCity.Pattern.FindCord(PosX-1,PosY-1)
                    if finded != None:
                        finded.Character = 'M'
                        finded.Health = int(Convoy.text)
                        NewCity.Military += 1
                    else:
                        print('La unidad militar con coordenadas ({},{}) no se pudo agregar'.format(PosX,PosY))

                CitiesList.InsertCity(NewCity)


    except:
        print('No se cargaron los datos correctamente del piso')



if __name__ == '__main__':
    ElementTree(file)
    CitiesList.ShowCities()