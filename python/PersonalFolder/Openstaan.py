import python.Query as Query
import python.Role.Assistant as Assistant
import python.Role.GeneralWorker as GeneralWorker
import python.Role.AllRounder as AllRounder
import python.Role.Vakspecialist as Vakspecialist


class Openstaan:

    #DEFINE PUBLIC FIELDS
    OpenstaanList = []
    OpenstaanAverageResult = []
    OpenstaanAchievedResult = []
    OpenstaanPassedResult = []
    OpenstaanFailedResult = []

    #Contructor
    def __init__(self, userId, averageResult, achievedResult, passed):
        self.userId = userId
        self.averageResult = averageResult
        self.achievedResult = achievedResult
        self.passed = passed

        #Class instances
        Openstaan.OpenstaanList.append([self.averageResult, self.achievedResult, self.passed])
        Openstaan.OpenstaanAverageResult.append(self.averageResult)
        Openstaan.OpenstaanAchievedResult.append(self.achievedResult)

        #passed formula
        if self.passed == 'Yes':
            Openstaan.OpenstaanPassedResult.append(self.passed)
        else:
            Openstaan.OpenstaanFailedResult.append(self.passed)

        role = Query.Query.getRoleOfUser(Query.Query, self.userId)
        if role == 1:
            Assistant.Assistant("openstaan", averageResult, achievedResult, passed)
        elif role == 2:
            GeneralWorker.GeneralWorker("openstaan", averageResult, achievedResult, passed)
        elif role == 3:
            AllRounder.AllRounder("openstaan", averageResult, achievedResult, passed)
        elif role == 4:
            Vakspecialist.Vakspecialist("openstaan", averageResult, achievedResult, passed)

    def getOpenstaanList(self):
        return self.OpenstaanList

    def getOpenstaanAverageResult(self):
        return self.OpenstaanAverageResult

    def getOpenstaanAchievedResult(self):
        return self.OpenstaanAchievedResult

    def getOpenstaanPassedResult(self):
        return self.OpenstaanPassedResult

    def getOpenstaanFailedResult(self):
        return self.OpenstaanFailedResult