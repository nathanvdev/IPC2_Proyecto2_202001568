from xml.dom import minidom

file = 'Docs/ArchivoPrueba.xml'

def MiniDom(file):
    try:
        domTree = minidom.parse(file)
        items = domTree.getElementsByTagName('ciudad')
        for element in items:
            print(element.getElementsByTagName('fila'), '\n')

    except:
        print('No se cargaron los datos correctamente del piso')



if __name__ == '__main__':
    MiniDom(file)