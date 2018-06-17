class PersonalQuery:

    #DEFINE PUBLIC FIELDS
    queryDataModel = ''

    #Contructor
    def __init__(self, queryData):
        #instance variables
        PersonalQuery.queryDataModel = queryData

    def getExtraversieAverageResult(self):
        return PersonalQuery.queryDataModel[0][2]

    def getExtraversieAchievedResult(self):
        return PersonalQuery.queryDataModel[0][3]

    def getOpenstaanAverageResult(self):
        return PersonalQuery.queryDataModel[1][2]

    def getOpenstaanAchievedResult(self):
        return PersonalQuery.queryDataModel[1][3]

    def getAanpassenAverageResult(self):
        return PersonalQuery.queryDataModel[2][2]

    def getAanpassenAchievedResult(self):
        return PersonalQuery.queryDataModel[2][3]

    def getInstabiliteitAverageResult(self):
        return PersonalQuery.queryDataModel[3][2]

    def getInstabiliteitAchievedResult(self):
        return PersonalQuery.queryDataModel[3][3]

    def getConscientieusheidAverageResult(self):
        return PersonalQuery.queryDataModel[4][2]

    def getConscientieusheidAchievedResult(self):
        return PersonalQuery.queryDataModel[4][3]