import python.Query as Query
import python.Role.Assistant as Assistant
import python.Role.GeneralWorker as GeneralWorker
import python.Role.AllRounder as AllRounder
import python.Role.Vakspecialist as Vakspecialist


class Instabiliteit:

    #DEFINE PUBLIC FIELDS
    InstabiliteitList = []
    InstabiliteitAverageResult = []
    InstabiliteitAchievedResult = []
    InstabiliteitPassedResult = []
    InstabiliteitFailedResult = []

    #Contructor
    def __init__(self, userId, averageResult, achievedResult, passed):
        self.userId = userId
        self.averageResult = averageResult
        self.achievedResult = achievedResult
        self.passed = passed

        Instabiliteit.InstabiliteitList.append([self.averageResult, self.achievedResult, self.passed])
        Instabiliteit.InstabiliteitAverageResult.append(self.averageResult)
        Instabiliteit.InstabiliteitAchievedResult.append(self.achievedResult)

        #passed formula
        if self.passed == 'Yes':
            Instabiliteit.InstabiliteitPassedResult.append(self.achievedResult)
        else:
            Instabiliteit.InstabiliteitFailedResult.append(self.achievedResult)

        role = Query.Query.getRoleOfUser(Query.Query, self.userId)
        if role == 1:
            Assistant.Assistant("instabiliteit", averageResult, achievedResult, passed)
        elif role == 2:
            GeneralWorker.GeneralWorker("instabiliteit", averageResult, achievedResult, passed)
        elif role == 3:
            AllRounder.AllRounder("instabiliteit", averageResult, achievedResult, passed)
        

    def getInstabiliteitList(self):
        return self.InstabiliteitList

    def getInstabiliteitAverageResult(self):
        return self.InstabiliteitAverageResult

    def getInstabiliteitAchievedResult(self):
        return self.InstabiliteitAchievedResult

    def getInstabiliteitPassedResult(self):
        return self.InstabiliteitPassedResult

    def getInstabiliteitFailedResult(self):
        return self.InstabiliteitFailedResult