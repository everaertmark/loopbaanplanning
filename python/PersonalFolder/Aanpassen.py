import python.Query as Query
import python.Role.Assistant as Assistant
import python.Role.GeneralWorker as GeneralWorker
import python.Role.AllRounder as AllRounder
import python.Role.Vakspecialist as Vakspecialist

class Aanpassen:

    #DEFINE PUBLIC FIELDS
    AanpassenList = []
    AanpassenAverageResult = []
    AanpassenAchievedResult = []
    AanpassenPassedResult = []
    AanpassenFailedResult = []

    #Contructor
    def __init__(self, userId, averageResult, achievedResult, passed):
        self.userId = userId
        self.averageResult = averageResult
        self.achievedResult = achievedResult
        self.passed = passed

        Aanpassen.AanpassenList.append([self.averageResult, self.achievedResult, self.passed])
        Aanpassen.AanpassenAverageResult.append(self.averageResult)
        Aanpassen.AanpassenAchievedResult.append(self.achievedResult)

        #passed formula
        if self.passed == 'Yes':
            Aanpassen.AanpassenPassedResult.append(self.passed)
        else:
            Aanpassen.AanpassenFailedResult.append(self.passed)

        role = Query.Query.getRoleOfUser(Query.Query, self.userId)
        if role == 1:
            Assistant.Assistant("aanpassen", averageResult, achievedResult, passed)
        elif role == 2:
            GeneralWorker.GeneralWorker("aanpassen", averageResult, achievedResult, passed)
        elif role == 3:
            AllRounder.AllRounder("aanpassen", averageResult, achievedResult, passed)
        elif role == 4:
            Vakspecialist.Vakspecialist("aanpassen", averageResult, achievedResult, passed)
        
    def getAanpassenList(self):
        return self.AanpassenList

    def getAanpassenAverageResult(self):
        return self.AanpassenAverageResult

    def getAanpassenAchievedResult(self):
        return self.AanpassenAchievedResult

    def getAanpassenPassedResult(self):
        return self.AanpassenPassedResult

    def getAanpassenFailedResult(self):
        return self.AanpassenFailedResult
