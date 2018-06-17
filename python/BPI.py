import python.GeneralBPI as GeneralBPI
import python.Role.Assistant as Assistant
import python.Role.GeneralWorker as GeneralWorker
import python.Role.AllRounder as AllRounder

import python.Query as Query

class BPI:

    #DEFINE PUBLIC FIELDS
    userList = []
    testList = []
    functionList = []
    roleList = []
    levelList = []
    averageResultList = []
    achievedResultList = []
    yearList = []

    #Contructor
    def __init__(self, userId, testId, function, role, level, average_result, achieved_result, year):
        #instance variables
        self.userId = userId
        self.testId = testId
        self.function = function
        self.role = role
        self.level = level
        self.average_result = average_result
        self.achieved_result = achieved_result
        self.year = year

        #class variables
        BPI.userList.append(self.userId)
        BPI.testList.append(self.testId)
        BPI.functionList.append(self.function)
        BPI.roleList.append(self.role)
        BPI.levelList.append(self.level)
        BPI.averageResultList.append(self.average_result)
        BPI.achievedResultList.append(self.achieved_result)
        BPI.yearList.append(self.year)

    def getUserList(self):
        return self.userList

    def getTestList(self):
        return self.testList

    def getFunctionList(self):
        return self.functionList

    def getRoleList(self):
        return self.roleList

    def getLevelList(self):
        return self.levelList

    def getAverageResultList(self):
        return self.averageResultList

    def getAchievedResultList(self):
        return self.achievedResultList

    def getYearList(self):
        return self.yearList
