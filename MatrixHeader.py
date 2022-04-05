class NodeHeader:
    def __init__(self, id):
        self.id = id
        self.Next = None
        self.Prev = None
        self.access = None
     
class HeaderList:

    def __init__(self, Type):
        self.First = None
        self.Last = None
        self.type = Type 
        self.size = 0
    

    def insertNodeHeader(self, nuevo : NodeHeader):
        self.size += 1
        if self.First == None:
            self.First = nuevo
            self.Last = nuevo
        else:
            if nuevo.id < self.First.id:
                nuevo.Next = self.First
                self.First.Prev = nuevo
                self.First = nuevo

            elif nuevo.id > self.Last.id:
                self.Last.Next = nuevo
                nuevo.Prev = self.Last
                self.Last = nuevo

            else:
                tmp: NodeHeader = self.First 
                while tmp != None:
                    if nuevo.id < tmp.id:
                        nuevo.Next = tmp
                        nuevo.Prev = tmp.Prev
                        tmp.Prev.Next = nuevo
                        tmp.Prev = nuevo
                        break

                    elif nuevo.id > tmp.id:
                        tmp = tmp.Next

                    else:
                        break

    
    def mostrarCabeceras(self):
        tmp = self.First
        while tmp != None:
            print('Cabecera', self.type, tmp.id)
            tmp = tmp.Next
            

    def getHeader(self, id): 
        tmp = self.First
        while tmp != None:
            if id == tmp.id:
                return tmp
            else:
                tmp = tmp.Next
        return None
    