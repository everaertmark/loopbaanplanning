import python.Query as Query
import python.Role.Assistant as Assistant
import python.Role.GeneralWorker as GeneralWorker
import python.Role.AllRounder as AllRounder
import python.Role.Vakspecialist as Vakspecialist

class Extraversie:

    #DEFINE PUBLIC FIELDS
    ExtraversieList = []
    ExtraversieAverageResult = []
    ExtraversieAchievedResult = []
    ExtraversiePassedResult = []
    ExtraversieFailedResult = []

    #Contructor
    def __init__(self, userId, averageResult, achievedResult, passed):
        self.userId = userId
        self.averageResult = averageResult
        self.achievedResult = achievedResult
        self.passed = passed

        Extraversie.ExtraversieList.append([self.averageResult, self.achievedResult, self.passed])
        Extraversie.ExtraversieAverageResult.append(self.averageResult)
        Extraversie.ExtraversieAchievedResult.append(self.achievedResult)

        #passed formula
        if self.passed == 'Yes':
            Extraversie.ExtraversiePassedResult.append(self.achievedResult)
        else:
            Extraversie.ExtraversieFailedResult.append(self.achievedResult)

        role = Query.Query.getRoleOfUser(Query.Query, self.userId)
        if role == 1:
            Assistant.Assistant("extraversie", averageResult, achievedResult, passed)
        elif role == 2:
            GeneralWorker.GeneralWorker("extraversie", averageResult, achievedResult, passed)
        elif role == 3:
            AllRounder.AllRounder("extraversie", averageResult, achievedResult, passed)
        elif role == 4:
            Vakspecialist.Vakspecialist("extraversie", averageResult, achievedResult, passed)


    def getExtraversieList(self):
        return self.ExtraversieList

    def getExtraversieAverageResult(self):
        return self.ExtraversieAverageResult

    def getExtraversieAchievedResult(self):
        return self.ExtraversieAchievedResult

    def getExtraversiePassedResult(self):
        return self.ExtraversiePassedResult

    def getExtraversieFailedResult(self):
        return self.ExtraversieFailedResult