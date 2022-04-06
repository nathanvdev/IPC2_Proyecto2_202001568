
from SparceMatrix import SparceMatrix


class NodeCity:
    def __init__(self, Name, Rows, Columns):
        self.Name = Name
        self.Rows = int(Rows)
        self.Columns = int(Columns)
        self.Size = self.Rows*self.Columns
        self.Pattern = SparceMatrix()
        self.Rescue = 0
        self.Extract = 0
        self.Next: NodeCity = None

class ListCities:
    def __init__(self):
        self.First: NodeCity = None
        self.Last: NodeCity = None
        self.Size = 0
    
    def InsertCity(self, NewCity: NodeCity):
        
        if self.First is None:
            self.First = NewCity
            self.Last = NewCity
            self.Size += 1
        else:
            tmp = self.First
            while tmp != None:
                if tmp.Name == NewCity.Name:
                    tmp.Rows = NewCity.Rows
                    tmp.Columns = NewCity.Columns
                    tmp.Size = NewCity.Size
                    tmp.Pattern = NewCity.Pattern
                    tmp.Rescue = NewCity.Rescue
                    tmp.Extract = NewCity.Extract
                    break
                elif tmp.Next is None:
                    self.Last.Next = NewCity
                    self.Last = NewCity
                    self.Size += 1
                else:
                    tmp = tmp.Next

            

    def ShowCities(self):
        tmp = self.First
        while tmp != None:
            print('>>>  ',tmp.Name)
            tmp = tmp.Next
    
    def FindCity(self, CityName):
        tmp = self.First
        while tmp != None:
            if CityName == tmp.Name:
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
    
    def showRobots(self, type):
        tmp = self.First
        while tmp.Next != None:
            if tmp.Type == type:
                if tmp.Type == 'ChapinRescue':
                    print('>>> Nombre:',tmp.Name)
                elif tmp.Type == 'ChapinFighter':
                    print('>>> Nombre:',tmp.Name, 'Vida:', tmp.Health)
            tmp = tmp.Next

    def FindRobot(self, Name):
        tmp = self.First
        while tmp != None:
            if tmp.Name == Name:
                return tmp
            tmp = tmp.Next
        print('No se encontro el robot')
        return None