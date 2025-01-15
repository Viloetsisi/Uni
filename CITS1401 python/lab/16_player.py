#class for player with static and non-static variables
class player:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    def setAge(self,age):
        self.age = age
    def getAge(self):
        return self.age
    def setSport(self,sport):
        player.sport = sport
    def getSport(self):
        return self.sport