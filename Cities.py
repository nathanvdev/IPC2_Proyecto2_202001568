from SparceMatrix import SparceMatrix


class NodeCity:
    def __init__(self, Name, Rows, Columns):
        self.Name = Name
        self.Rows = int(Rows)
        self.Columns = int(Columns)
        self.Size = self.Rows*self.Columns
        self.Pattern = SparceMatrix()
        self.Military = 0
        self.Next: NodeCity = None

class ListCities:
    def __init__(self):
        self.First: NodeCity = None
        self.Last: NodeCity = None
        self.Size = 0
    
    def InsertCity(self, NewCity):
        self.Size += 1
        if self.First is None:
            self.First = NewCity
            self.Last = NewCity
        else:
            self.Last.Next = NewCity
            self.Last = NewCity

    def ShowCities(self):
        tmp = self.First
        while tmp != None:
            print(tmp.Name)
            tmp.Pattern.RowsIteration()
            tmp = tmp.Next

