class AllRounder:

    #DEFINE PUBLIC FIELDS
    ExtraversieList = []
    ExtraversieAverageResult = []
    ExtraversieAchievedResult = []
    ExtraversiePassedResult = []
    ExtraversieFailedResult = []

    OpenstaanList = []
    OpenstaanAverageResult = []
    OpenstaanAchievedResult = []
    OpenstaanPassedResult = []
    OpenstaanFailedResult = []

    AanpassenList = []
    AanpassenAverageResult = []
    AanpassenAchievedResult = []
    AanpassenPassedResult = []
    AanpassenFailedResult = []

    InstabiliteitList = []
    InstabiliteitAverageResult = []
    InstabiliteitAchievedResult = []
    InstabiliteitPassedResult = []
    InstabiliteitFailedResult = []

    ConscientieusheidList = []
    ConscientieusheidAverageResult = []
    ConscientieusheidAchievedResult = []
    ConscientieusheidPassedResult = []
    ConscientieusheidFailedResult = []

    #Contructor
    def __init__(self, karakter, averageResult, achievedResult, passed):
        self.karakter = karakter
        self.averageResult = averageResult
        self.achievedResult = achievedResult
        self.passed = passed

        if self.karakter == 'extraversie':
            AllRounder.ExtraversieList.append([self.averageResult, self.achievedResult, self.passed])
            AllRounder.ExtraversieAverageResult.append(self.averageResult)
            AllRounder.ExtraversieAchievedResult.append(self.achievedResult)
            # passed formula
            if self.passed == 'Yes':
                AllRounder.ExtraversiePassedResult.append(self.achievedResult)
            else:
                AllRounder.ExtraversieFailedResult.append(self.achievedResult)
        elif self.karakter == 'openstaan':
            AllRounder.OpenstaanList.append([self.averageResult, self.achievedResult, self.passed])
            AllRounder.OpenstaanAverageResult.append(self.averageResult)
            AllRounder.OpenstaanAchievedResult.append(self.achievedResult)
            # passed formula
            if self.passed == 'Yes':
                AllRounder.OpenstaanPassedResult.append(self.achievedResult)
            else:
                AllRounder.OpenstaanFailedResult.append(self.achievedResult)
        elif self.karakter == 'aanpassen':
            AllRounder.AanpassenList.append([self.averageResult, self.achievedResult, self.passed])
            AllRounder.AanpassenAverageResult.append(self.averageResult)
            AllRounder.AanpassenAchievedResult.append(self.achievedResult)
            # passed formula
            if self.passed == 'Yes':
                AllRounder.AanpassenPassedResult.append(self.achievedResult)
            else:
                AllRounder.AanpassenFailedResult.append(self.achievedResult)
        elif self.karakter == 'instabiliteit':
            AllRounder.InstabiliteitList.append([self.averageResult, self.achievedResult, self.passed])
            AllRounder.InstabiliteitAverageResult.append(self.averageResult)
            AllRounder.InstabiliteitAchievedResult.append(self.achievedResult)
            # passed formula
            if self.passed == 'Yes':
                AllRounder.InstabiliteitPassedResult.append(self.achievedResult)
            else:
                AllRounder.InstabiliteitFailedResult.append(self.achievedResult)
        elif self.karakter == 'conscientieusheid':
            AllRounder.ConscientieusheidList.append([self.averageResult, self.achievedResult, self.passed])
            AllRounder.ConscientieusheidAverageResult.append(self.averageResult)
            AllRounder.ConscientieusheidAchievedResult.append(self.achievedResult)
            # passed formula
            if self.passed == 'Yes':
                AllRounder.ConscientieusheidPassedResult.append(self.achievedResult)
            else:
                AllRounder.ConscientieusheidFailedResult.append(self.achievedResult)

    def wipeAllRounderResults(self):
        AllRounder.ExtraversieList = []
        AllRounder.ExtraversieAverageResult = []
        AllRounder.ExtraversieAchievedResult = []
        AllRounder.ExtraversiePassedResult = []
        AllRounder.ExtraversieFailedResult = []

        AllRounder.OpenstaanList = []
        AllRounder.OpenstaanAverageResult = []
        AllRounder.OpenstaanAchievedResult = []
        AllRounder.OpenstaanPassedResult = []
        AllRounder.OpenstaanFailedResult = []

        AllRounder.AanpassenList = []
        AllRounder.AanpassenAverageResult = []
        AllRounder.AanpassenAchievedResult = []
        AllRounder.AanpassenPassedResult = []
        AllRounder.AanpassenFailedResult = []

        AllRounder.InstabiliteitList = []
        AllRounder.InstabiliteitAverageResult = []
        AllRounder.InstabiliteitAchievedResult = []
        AllRounder.InstabiliteitPassedResult = []
        AllRounder.InstabiliteitFailedResult = []

        AllRounder.ConscientieusheidList = []
        AllRounder.ConscientieusheidAverageResult = []
        AllRounder.ConscientieusheidAchievedResult = []
        AllRounder. ConscientieusheidPassedResult = []
        AllRounder.ConscientieusheidFailedResult = []

    #Extraversie methods
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

    #Openstaan methods
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

    #Aanpassen methods
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

    #Instabiliteit methods
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

    #Conscientieusheid methods
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