from __future__ import print_function
import os, webbrowser
from queue import PriorityQueue
from tkinter import Tk, filedialog
from xml.etree import ElementTree as ET
from Cities import ListCities, NodeCity, NodeRobot, RobotListP



CitiesList = ListCities()
RobotList = RobotListP()

def FileChooser():
    Tk().withdraw()
    try:
        filename = filedialog.askopenfile(
            initialdir = './',
            title = 'Selecciona un archivo',
            filetypes = (('Archivos xml', "*.{}".format('xml')),
                         ('Todos los archivos', '*.*'))
        )
        return filename
    except:
        print('No se selecciono correctamente el archivo')
        return None


def ElementTree(file):
    try:
        tree = ET.parse(file)
        root = tree.getroot()
        for element in root:
            Robot = element.findall('robot')
            cities = element.findall('ciudad')
            for City in cities:
                CityName = City.find('nombre')
                CityRows = City.findall('fila')
                CityConvoys = City.findall('unidadMilitar')

                
                
                NewCity = NodeCity(CityName.text, CityName.attrib['filas'], CityName.attrib['columnas'])
                
                
                
                for Row in CityRows:
                    patron = Row.text.replace('"','')
                    patron = patron.upper()
                    PosX = 0
                    PosY = int(Row.attrib['numero'])
                    PosY = PosY -1
                    for character in patron:
                        if character != '*':
                            if character.upper() == 'C':
                                NewCity.Rescue += 1
                            elif character.upper() == 'R':
                                NewCity.Extract += 1
                            NewCity.Pattern.Insert(PosX, PosY, character)
                        PosX += 1    
                            
                for Convoy in CityConvoys:
                    PosX = int(Convoy.attrib['columna'])
                    PosY = int(Convoy.attrib['fila'])
                    finded = NewCity.Pattern.FindCord(PosX-1,PosY-1)
                    if finded != None:
                        finded.Character = 'M'
                        finded.Health = int(Convoy.text)

                    else:
                        print('La unidad militar con coordenadas ({},{}) no se pudo agregar'.format(PosX,PosY))

                CitiesList.InsertCity(NewCity)

            
            for x in Robot:
                Robots = x.findall('nombre')
                for r in Robots:
                    if r.attrib['tipo'].lower() == 'chapinfighter':
                        RobotList.InsertRobot(r.text, r.attrib['tipo'], r.attrib['capacidad'])
                    else:
                        RobotList.InsertRobot(r.text, r.attrib['tipo'], None)

        
        
    except:
        print('No se cargaron los datos correctamente del Archivo')



    
def Graphviz(Selected: NodeCity, Mission, CordXM, CordYM, Robot: NodeRobot, CordXE, CordYE):
    txt = '''digraph Grafica{
graph [pad="0.5" bgcolor="#E4A63A" style="filled" margin="0"]
fontname="times-bold" fontsize="20pt" node [style = filled shape = box height="1" width="1"]

'''
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


    txt += '\nlabel="'
    txt += 'Ciudad: {}\n'.format(Selected.Name)
    txt += 'Tipo de Mision: {}\n'.format(Mission)
    txt += 'Unidad Rescatada: ({},{}) (x,y)\n'.format(CordXM, CordYM)
    txt += 'Robot: {}\n'.format(Robot.Name)
    if Robot.Health is not None:
        txt += 'Vida actual del Robot: {}\n'.format(Robot.Health)
    txt += 'Entrada: ({},{}) (x,y)\n'.format(CordXE, CordYE)
    txt += 'Nathan Valdez --- 202001568"\n}'

    dot = "Ciudad-{}.txt".format(Selected.Name)
    with open(dot, 'w') as grafo:
        grafo.write(txt)
    result = "Ciudad-{}.png".format(Selected.Name)
    os.system("neato -Tpng " + dot + " -o " + result)
    webbrowser.open(result) 

if __name__ == '__main__':
    while True:
        Menu = input ('''
==================================
|| 1. Cargar Archivo XML        ||
|| 2. Mostrar Ciudades Cargadas ||
|| 9. Salir                     ||
==================================
Elige una opción:  ------->  ''')

        if Menu == '9':
            break

        if Menu == '1':
            file = FileChooser()
            ElementTree(file)
        
        if Menu == '2':
            CitiesList.ShowCities()

            while True:
                Menu2 = input('''
====================================
|| >> Para Seleccionar una ciudad  ||
||    Escriba el Nombre            ||
|| 9. Regresar                     ||
====================================
Elige una opción:  ------->  ''')
                
                if Menu2 == '9':
                    break

                else:
                    CitySelected = CitiesList.FindCity(Menu2)
                    if CitySelected is None: 
                        print('Ciudad "{}" no encontrada',format(Menu2))
                    elif CitySelected is not None:
                        while True:
                            Menu3 = input('''
⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨
⩨  Misiones Disponibles:                 ⩨
⩨  1. Mision de Rescate     |Total:{}     ⩨
⩨  2. Mision de Extraccion  |Total:{}     ⩨
⩨  9. Regresar                           ⩨
⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨⩨
Elige una opción:  ------->  '''.format(CitySelected.Rescue, CitySelected.Extract))

                            if Menu3 == '9':
                                break

                            elif Menu3 == '1':
                                if CitySelected.Rescue > 1:
                                    print('\n Rescates Disponibles:')
                                    CitySelected.Pattern.PrintMissions('C')
                                    while True:
                                        CordX = input('''
=====================================
|| >> Para Seleccionar un Rescate   ||
||    Escriba pirmero la coordenada ||
||    En X & luego la coordenada    ||
||    en Y                          ||
|| Q. Regresar                      ||
=====================================
Coordenada en X:  ------->  ''')
                                        if CordX.upper() == 'Q':
                                            break

                                        CordY = input('''
=====================================
|| Q. Regresar                      ||
=====================================
Coordenada en Y:  ------->  ''')
                                        if CordY.upper() == 'Q':
                                            break

                                        else:
                                            Select = CitySelected.Pattern.FindCord(int(CordX), int(CordY))
                                            if Select is not None:
                                                print('Seleccionado Correctamente!!!')
                                                if RobotList.CountRescue < 1:
                                                    print('\nMision Fallida')
                                                    break

                                                elif RobotList.CountRescue > 0:
                                                    while True:
                                                        print('\nRobots Disponibles:')
                                                        RobotList.showRobots('ChapinRescue')
                                                        NameRobot = input('''
=====================================
|| >> Para Seleccionar un Robot     ||
||    Escriba el nombre             ||
|| Q. Regresar                      ||
=====================================
Nombre del Robot:  ------->  ''')
                                                        if NameRobot.upper() == 'Q':
                                                            break
                                                        else:
                                                            SelectedRobot = RobotList.FindRobot(NameRobot)
                                                            if SelectedRobot is not None:

                                                                print('Puntos de Entrada Disponibles')
                                                                CitySelected.Pattern.PrintMissions('E')
                                                                while True:
                                                                    CordXE = input('''
=====================================
|| >> Para seleccionar un punto de  ||
||    entrada escriba pirmero la    ||
||    coordenada En X & luego la    ||
||    coordenada en Y               ||
|| Q. Regresar                      ||
=====================================
Coordenada en X:  ------->  ''')
                                                                    if CordXE.upper() == 'Q':
                                                                        break

                                                                    CordYE = input('''
=====================================
|| Q. Regresar                      ||
=====================================
Coordenada en Y:  ------->  ''')
                                                                    if CordY.upper() == 'Q':
                                                                        break
                                                                    else:
                                                                        EntrySelected = CitySelected.Pattern.FindCord(int(CordXE),int(CordYE))
                                                                        if EntrySelected is not None:
                                                                            print('Mision Completada')
                                                                            Graphviz(CitySelected,'Rescate',CordX, CordY,SelectedRobot,CordXE,CordYE)
                                                                            break
                                                                        break
                                                                    
                            elif Menu3 == '2':
                                while True:
                                    Menu4 = input ('''
===================================
|| 1. Seleccionar Recurso        ||
|| 2. Seleccionar Robot          ||
|| 3. Seleccionar Entrada        ||
|| 9. Salir                      ||
===================================
Elige una opción:  ------->  ''')

                                    if Menu4 == '9':  
                                        break
                                    elif Menu4 == '1':
                                        while True:
                                            print('\n Extracciones Disponibles:')
                                            CitySelected.Pattern.PrintMissions('R')
                                            ExCordX = input ('''
=====================================
|| >> Para Seleccionar un Rescate   ||
||    Escriba pirmero la coordenada ||
||    En X & luego la coordenada    ||
||    en Y                          ||
|| Q. Regresar                      ||
=====================================
Coordenada en X:  ------->  ''')
                                            if ExCordX.upper() == 'Q':
                                                break
                                            ExCordY = input ('''
=====================================
|| Q. Regresar                      ||
=====================================
Coordenada en Y:  ------->  ''')
                                            if ExCordY.upper() == 'Q':
                                                break
                                            else:
                                                SelectedExtract = CitySelected.Pattern.FindCord(int(ExCordX), int(ExCordY))
                                                if SelectedExtract is not None:
                                                    print('Coordenada Encontrada')
                                                    break
                                                else:
                                                    print("Coordenadas Incorrectas")
                                    
                                    elif Menu4 == '2':
                                        while True:
                                            if RobotList.CountFighter < 1 :
                                                print("Mision Fallida, No hay robots disponibles")
                                            else:
                                                print('\nRobots Disponibles:')
                                                RobotList.showRobots('ChapinFighter')
                                                EXnameRobot = input('''
=====================================
|| >> Para Seleccionar un Robot     ||
||    Escriba el nombre             ||
|| Q. Regresar                      ||
=====================================
Nombre del Robot:  ------->  ''')
                                            if EXnameRobot.upper() == 'Q':
                                                break
                                            else:
                                                ExSelectedBot = RobotList.FindRobot(EXnameRobot)
                                                if ExSelectedBot is not None:
                                                    print('Robot Encontrado')
                                                    break
                                                else:
                                                    pass

                                    elif Menu4 == '3':
                                        while True:
                                            print('Puntos de Entrada Disponibles')
                                            CitySelected.Pattern.PrintMissions('E')
                                            while True:
                                                EntradaX = input('''
=====================================
|| >> Para seleccionar un punto de  ||
||    entrada escriba pirmero la    ||
||    coordenada En X & luego la    ||
||    coordenada en Y               ||
|| Q. Regresar                      ||
=====================================
Coordenada en X:  ------->  ''')
                                                if EntradaX.upper() == 'Q':
                                                    break

                                                EntradaY = input('''
=====================================
|| Q. Regresar                      ||
=====================================
Coordenada en Y:  ------->  ''')
                                                if EntradaY.upper() == 'Q':
                                                    break
                                                else:
                                                    ExEntry = CitySelected.Pattern.FindCord(int(EntradaX), int(EntradaY))
                                                    if ExEntry is not None:
                                                        print('Mision Completada')
                                                        Graphviz(CitySelected,'Extraccion',ExCordX, ExCordY,ExSelectedBot,EntradaX,EntradaY)
                                                        break
                    

