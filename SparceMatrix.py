from re import T
from MatrixHeader import NodeHeader, HeaderList

class MatrixNode(): 
    def __init__(self, x, y, Character):
        self.Character = Character
        self.Xcord = x  
        self.Ycord = y  
        self.up: MatrixNode = None
        self.down: MatrixNode = None
        self.right: MatrixNode = None  
        self.left: MatrixNode = None  


class SparceMatrix():
    def __init__(self):
        self.Row = HeaderList('Row')
        self.Column = HeaderList('Column')

    def Insert(self, PosX, PosY, Character):
        NewNode = MatrixNode(PosX, PosY, Character)
        NodeY = self.Row.getHeader(PosY)
        NodeX = self.Column.getHeader(PosX)

        if NodeX is None:
            NodeX = NodeHeader(PosX)
            self.Column.insertNodeHeader(NodeX)

        if NodeY is None:
            NodeY = NodeHeader(PosY)
            self.Row.insertNodeHeader(NodeY)

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
                tmp = NodeX.access
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
                tmp2 = NodeY.access
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
                    
    def RowIteration(self):
        tmp: NodeHeader = self.Row.First
        while tmp != None:
            tmp2: MatrixNode = tmp.access
            while tmp2 != None:
                print('({},{})'.format(tmp2.Xcord,tmp2.Ycord), end='|')
                tmp2 = tmp2.right
            print()
            tmp = tmp.Next

    def ColumnIteration(self):
        tmp: NodeHeader = self.Column.First
        while tmp != None:
            tmp2: MatrixNode = tmp.access
            while tmp2 != None:
                print('({},{})'.format(tmp2.Xcord,tmp2.Ycord), end='|')
                tmp2 = tmp2.down
            print()
            tmp = tmp.Next