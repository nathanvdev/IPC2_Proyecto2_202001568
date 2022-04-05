from xml.dom.minidom import parse

file = 'Docs/ArchivoPrueba.xml'

def MiniDom(file):
    try:
        domTree = parse("./customer.xml")
        rootNode = domTree.documentElement
	    print(rootNode.nodeName)

    except:
        print('No se cargaron los datos correctamente del piso')