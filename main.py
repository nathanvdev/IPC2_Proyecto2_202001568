import os
from traceback import print_tb
from typing import final
import webbrowser
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
                    patron = patron.upper()
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
    
def Graphviz(City):
    txt = '''digraph Grafica{
graph [pad="0.5" bgcolor="#E4A63A" style="filled" margin="0"]

fontname="times-bold" fontsize="20pt" node [style = filled shape = box height="1" width="1"] 
'''
    Selected = CitiesList.FindCity(City)

    if Selected != None:
        for PosY in range(Selected.Columns):
            for PosX in range(Selected.Rows):
                Node = Selected.Pattern.FindCord(PosX, PosY)
                if Node != None:
                    if Node.Character == ' ':
                        txt +='Node{}_{}[fillcolor= "#FFFFFF" fontcolor = "#FFFFFF" pos="{},-{}!"]\n'.format(PosX, PosY, PosX, PosY)
                    elif Node.Character == 'C':
                        txt += 'Node{}_{}[fillcolor= "#096F9B" fontcolor = "#096F9B" pos="{},-{}!"]\n'.format(PosX, PosY, PosX, PosY)
                    elif Node.Character == 'M':
                        txt += 'Node{}_{}[fillcolor= "#952D2D" fontcolor = "#952D2D" pos="{},-{}!"]\n'.format(PosX, PosY, PosX, PosY)
                    elif Node.Character == 'R':
                        txt += 'Node{}_{}[fillcolor= "#FF7400" fontcolor = "#FF7400" pos="{},-{}!"]\n'.format(PosX, PosY, PosX, PosY)
                    elif Node.Character == 'E':
                        txt += 'Node{}_{}[fillcolor= "#096E06" fontcolor = "#096E06" pos="{},-{}!"]\n'.format(PosX, PosY, PosX, PosY)
                else:
                    txt += 'Node{}_{}[fillcolor= "#000000" fontcolor = "#000000" pos="{},-{}!"]\n'.format(PosX, PosY, PosX, PosY)

    txt+='''label = "
Nathan Valdez --- 202001568"
}'''

    dot = "Ciudad-{}.txt".format(Selected.Name)
    with open(dot, 'w') as grafo:
        grafo.write(txt)
    result = "Ciudad-{}.png".format(Selected.Name)
    os.system("neato -Tpng " + dot + " -o " + result)
    # os.system('neato -Tpng ' + dot + ' -o ' + result)
    webbrowser.open(result) 

if __name__ == '__main__':
    ElementTree(file)
    CitiesList.ShowCities()
    Graphviz('Atlantis')