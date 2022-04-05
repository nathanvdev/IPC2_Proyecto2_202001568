

file = 'Docs/ArchivoPrueba.xml'

def ElementTree(file):
    try:
        tree = ET.parse(file)
        root = tree.getroot()
        for element in root:
            name = element.attrib['nombre']
            row = ''
            column = ''
            flip = ''
            slide = ''
            for subelement in element:
                tag = str(subelement.tag).lower()
                if tag == 'r':
                    row = int(subelement.text)
                elif tag == 'c':
                    column = int(subelement.text)
                elif tag == 'f':
                    flip = int(subelement.text)
                elif tag == 's':
                    slide = int(subelement.text)
                elif tag == 'patrones':
                    patrones = subelement
                else:
                    print('Atributo no registrable', subelement.tag)
            if row >= 1 and column >= 1 and flip >= 0 and slide >= 0:
                FloorList1.AddFloor(name, row, column, flip, slide, patrones)
                print('piso "{}" cargado correctamente'.format(element.attrib['nombre']))
            else:
                print('!!!ERROR!!! Datos del piso "{}" incorrectos'.format(element.attrib['nombre']))
    except:
        print('No se cargaron los datos correctamente del piso "{}"'.format(element.attrib['nombre']))