class Assistant:

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
            Assistant.ExtraversieList.append([self.averageResult, self.achievedResult, self.passed])
            Assistant.ExtraversieAverageResult.append(self.averageResult)
            Assistant.ExtraversieAchievedResult.append(self.achievedResult)
            # passed formula
            if self.passed == 'Yes':
                Assistant.ExtraversiePassedResult.append(self.achievedResult)
            else:
                Assistant.ExtraversieFailedResult.append(self.achievedResult)
        elif self.karakter == 'openstaan':
            Assistant.OpenstaanList.append([self.averageResult, self.achievedResult, self.passed])
            Assistant.OpenstaanAverageResult.append(self.averageResult)
            Assistant.OpenstaanAchievedResult.append(self.achievedResult)
            # passed formula
            if self.passed == 'Yes':
                Assistant.OpenstaanPassedResult.append(self.achievedResult)
            else:
                Assistant.OpenstaanFailedResult.append(self.achievedResult)
        elif self.karakter == 'aanpassen':
            Assistant.AanpassenList.append([self.averageResult, self.achievedResult, self.passed])
            Assistant.AanpassenAverageResult.append(self.averageResult)
            Assistant.AanpassenAchievedResult.append(self.achievedResult)
            # passed formula
            if self.passed == 'Yes':
                Assistant.AanpassenPassedResult.append(self.achievedResult)
            else:
                Assistant.AanpassenFailedResult.append(self.achievedResult)
        elif self.karakter == 'instabiliteit':
            Assistant.InstabiliteitList.append([self.averageResult, self.achievedResult, self.passed])
            Assistant.InstabiliteitAverageResult.append(self.averageResult)
            Assistant.InstabiliteitAchievedResult.append(self.achievedResult)
            # passed formula
            if self.passed == 'Yes':
                Assistant.InstabiliteitPassedResult.append(self.achievedResult)
            else:
                Assistant.InstabiliteitFailedResult.append(self.achievedResult)
        elif self.karakter == 'conscientieusheid':
            Assistant.ConscientieusheidList.append([self.averageResult, self.achievedResult, self.passed])
            Assistant.ConscientieusheidAverageResult.append(self.averageResult)
            Assistant.ConscientieusheidAchievedResult.append(self.achievedResult)
            # passed formula
            if self.passed == 'Yes':
                Assistant.ConscientieusheidPassedResult.append(self.achievedResult)
            else:
                Assistant.ConscientieusheidFailedResult.append(self.achievedResult)

    def wipeAssistantResults(self):
        Assistant.ExtraversieList = []
        Assistant.ExtraversieAverageResult = []
        Assistant.ExtraversieAchievedResult = []
        Assistant.ExtraversiePassedResult = []
        Assistant.ExtraversieFailedResult = []

        Assistant.OpenstaanList = []
        Assistant.OpenstaanAverageResult = []
        Assistant.OpenstaanAchievedResult = []
        Assistant.OpenstaanPassedResult = []
        Assistant.OpenstaanFailedResult = []

        Assistant.AanpassenList = []
        Assistant.AanpassenAverageResult = []
        Assistant.AanpassenAchievedResult = []
        Assistant.AanpassenPassedResult = []
        Assistant.AanpassenFailedResult = []

        Assistant.InstabiliteitList = []
        Assistant.InstabiliteitAverageResult = []
        Assistant.InstabiliteitAchievedResult = []
        Assistant.InstabiliteitPassedResult = []
        Assistant.InstabiliteitFailedResult = []

        Assistant.ConscientieusheidList = []
        Assistant.ConscientieusheidAverageResult = []
        Assistant.ConscientieusheidAchievedResult = []
        Assistant. ConscientieusheidPassedResult = []
        Assistant.ConscientieusheidFailedResult = []

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