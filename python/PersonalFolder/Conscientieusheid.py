import python.Query as Query
import python.Role.Assistant as Assistant
import python.Role.GeneralWorker as GeneralWorker
import python.Role.AllRounder as AllRounder
import python.Role.Vakspecialist as Vakspecialist

class Conscientieusheid:

    #DEFINE PUBLIC FIELDS
    ConscientieusheidList = []
    ConscientieusheidAverageResult = []
    ConscientieusheidAchievedResult = []
    ConscientieusheidPassedResult = []
    ConscientieusheidFailedResult = []

    #Contructor
    def __init__(self, userId, averageResult, achievedResult, passed):
        self.userId = userId
        self.averageResult = averageResult
        self.achievedResult = achievedResult
        self.passed = passed

        Conscientieusheid.ConscientieusheidList.append([self.averageResult, self.achievedResult, self.passed])
        Conscientieusheid.ConscientieusheidAverageResult.append(self.averageResult)
        Conscientieusheid.ConscientieusheidAchievedResult.append(self.achievedResult)

        #passed formula
        if self.passed == 'Yes':
            Conscientieusheid.ConscientieusheidPassedResult.append(self.passed)
        else:
            Conscientieusheid.ConscientieusheidFailedResult.append(self.passed)

        role = Query.Query.getRoleOfUser(Query.Query, self.userId)
        if role == 1:
            Assistant.Assistant("conscientieusheid", averageResult, achievedResult, passed)
        elif role == 2:
            GeneralWorker.GeneralWorker("conscientieusheid", averageResult, achievedResult, passed)
        elif role == 3:
            AllRounder.AllRounder("conscientieusheid", averageResult, achievedResult, passed)
        elif role == 4:
            Vakspecialist.Vakspecialist("conscientieusheid", averageResult, achievedResult, passed)
        

    def getConscientieusheidList(self):
        return self.ConscientieusheidList

    def getConscientieusheidAverageResult(self):
        return self.ConscientieusheidAverageResult

    def getConscientieusheidAchievedResult(self):
        return self.ConscientieusheidAchievedResult

    def getConscientieusheidPassedResult(self):
        return self.ConscientieusheidPassedResult

    def getConscientieusheidFailedResult(self):
        return self.ConscientieusheidFailedResult