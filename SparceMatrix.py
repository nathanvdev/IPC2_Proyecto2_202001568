from ast import Try
from email import header
from queue import PriorityQueue
from re import T
from MatrixHeader import NodeHeader, HeaderList

class MatrixNode(): 
    def __init__(self, x, y, Character):
        self.Character = Character
        self.Xcord = x  
        self.Ycord = y  
        self.Health = None
        self.up: MatrixNode = None
        self.down: MatrixNode = None
        self.right: MatrixNode = None  
        self.left: MatrixNode = None  


class SparceMatrix():
    def __init__(self):
        self.Rows = HeaderList('Rows')
        self.Columns = HeaderList('Columns')

    def Insert(self, PosX, PosY, Character):
        NewNode = MatrixNode(PosX, PosY, Character)
        NodeY = self.Rows.getHeader(PosY)
        NodeX = self.Columns.getHeader(PosX)

        if NodeX is None:
            NodeX = NodeHeader(PosX)
            self.Columns.insertNodeHeader(NodeX)

        if NodeY is None:
            NodeY = NodeHeader(PosY)
            self.Rows.insertNodeHeader(NodeY)

        if NodeX.access is None:
            NodeX.access = NewNode
        else:
            if NewNode.Ycord < NodeX.access.Ycord:
                NewNode.down = NodeX.access
                NodeX.access.up = NewNode
                NodeX.access = NewNode

            elif NewNode.Ycord == NodeX.access.Ycord and NewNode.Xcord == NodeX.access.Xcord:
                NodeX.access.Character = NewNode.Character

            else:
                tmp: MatrixNode = NodeX.access
                while tmp is not None:
                    if NewNode.Ycord < tmp.Ycord:
                        NewNode.up = tmp.up
                        NewNode.down = tmp
                        tmp.up.down = NewNode
                        tmp.up = NewNode
                        break

                    elif NewNode.Ycord == tmp.Ycord and NewNode.Xcord == tmp.Xcord:
                        tmp.Character = NewNode.Character
                        break

                    else:
                        if tmp.down is None:
                            NewNode.up = tmp
                            tmp.down = NewNode
                            break
                        else:
                            tmp = tmp.down

        if NodeY.access is None:
            NodeY.access = NewNode
        else:
            if NewNode.Xcord < NodeY.access.Xcord:
                NewNode.right = NodeY.access
                NodeY.access.left = NewNode
                NodeY.access = NewNode

            elif NewNode.Xcord == NodeY.access.Xcord and NewNode.Ycord == NodeY.access.Ycord:
                NodeY.access.Character = NewNode.Character

            else:
                tmp2: MatrixNode = NodeY.access
                while tmp2 is not None:
                    if NewNode.Xcord < tmp2.Xcord:
                        NewNode.left = tmp2.left
                        NewNode.right = tmp2
                        tmp2.left.right = NewNode
                        tmp2.left = NewNode
                        break

                    elif NewNode.Xcord == tmp2.Xcord and NewNode.Ycord == tmp2.Ycord:
                        tmp2.Character = NewNode.Character
                        break
                    
                    else:
                        if tmp2.right is None:
                            NewNode.left = tmp2
                            tmp2.right = NewNode
                            break
                        else:
                            tmp2 = tmp2.right
                    
    def RowsIteration(self):
        tmp: NodeHeader = self.Rows.First
        while tmp != None:
            tmp2: MatrixNode = tmp.access
            while tmp2 != None:
                print('({},{}) [{}]'.format(tmp2.Xcord,tmp2.Ycord,tmp2.Character), end='|')
                tmp2 = tmp2.right
            print()
            tmp = tmp.Next

    def ColumnsIteration(self):
        tmp: NodeHeader = self.Columns.First
        while tmp != None:
            tmp2: MatrixNode = tmp.access
            while tmp2 != None:
                print('({},{})'.format(tmp2.Xcord,tmp2.Ycord), end='|')
                tmp2 = tmp2.down
            print()
            tmp = tmp.Next

    def FindCord(self, CordX, CordY):
        try:
            tmp: MatrixNode = self.Rows.getHeader(CordY).access
            while tmp != None:
                if tmp.Xcord == CordX and tmp.Ycord == CordY:
                    return tmp
                tmp = tmp.right
        except:
            print('No se encontro ({},{})'.format(CordX,CordY))
            return None

    def PrintMissions(self, character):
        try:
            header = self.Rows.First
            while header is not None:
                tmp: MatrixNode = header.access
                while tmp is not None:
                    if tmp.Character == character:
                        print('>> Coordenadas (x,y) ({},{})'.format(tmp.Xcord, tmp.Ycord))
                    tmp = tmp.right
                header = header.Next
        except:
            pass


        
    def FindMission(self, character):
        try:
            header = self.Rows.First
            while header is not None:
                tmp: MatrixNode = header.access
                while tmp is not None:
                    if tmp.Character == character:
                        return tmp
                    tmp = tmp.right
                header = header.Next
        except:
            pass