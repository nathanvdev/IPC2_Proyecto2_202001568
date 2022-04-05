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
    
    def FindCity(self, City):
        tmp = self.First
        while tmp != None:
            if City == tmp.Name:
                return tmp
            tmp = tmp.Next
        return None


class NodeRobot:
    def __init__(self, Name, Type):
        self.Name = Name
        self.Health = None
        self.Type = Type
        self.Next: NodeRobot = None


class RobotListP:
    def __init__(self):
        self.First: NodeRobot = None
        self.CountRescue = 0 
        self.CountFighter = 0

    def InsertRobot(self, Name, Type, Health):
        NewRobot = NodeRobot(Name, Type)
        if self.First is None:
            self.First = NewRobot
        else:
            tmp = self.First
            while tmp.Next != None:
                tmp = tmp.Next
            tmp.Next = NewRobot
        if NewRobot.Type == 'ChapinFighter':
            self.CountFighter += 1
            NewRobot.Health = Health
        elif NewRobot.Type == "ChapinRescue":
            self.CountRescue += 1
    
    def showRobots(self):
        tmp = self.First
        while tmp.Next != None:
            print(tmp.Name, '-', tmp.Health, '-', tmp.Type)
            tmp = tmp.Next