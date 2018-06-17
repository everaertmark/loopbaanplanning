class Vakspecialist:

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
            Vakspecialist.ExtraversieList.append([self.averageResult, self.achievedResult, self.passed])
            Vakspecialist.ExtraversieAverageResult.append(self.averageResult)
            Vakspecialist.ExtraversieAchievedResult.append(self.achievedResult)
            # passed formula
            if self.passed == 'Yes':
                Vakspecialist.ExtraversiePassedResult.append(self.achievedResult)
            else:
                Vakspecialist.ExtraversieFailedResult.append(self.achievedResult)
        elif self.karakter == 'openstaan':
            Vakspecialist.OpenstaanList.append([self.averageResult, self.achievedResult, self.passed])
            Vakspecialist.OpenstaanAverageResult.append(self.averageResult)
            Vakspecialist.OpenstaanAchievedResult.append(self.achievedResult)
            # passed formula
            if self.passed == 'Yes':
                Vakspecialist.OpenstaanPassedResult.append(self.achievedResult)
            else:
                Vakspecialist.OpenstaanFailedResult.append(self.achievedResult)
        elif self.karakter == 'aanpassen':
            Vakspecialist.AanpassenList.append([self.averageResult, self.achievedResult, self.passed])
            Vakspecialist.AanpassenAverageResult.append(self.averageResult)
            Vakspecialist.AanpassenAchievedResult.append(self.achievedResult)
            # passed formula
            if self.passed == 'Yes':
                Vakspecialist.AanpassenPassedResult.append(self.achievedResult)
            else:
                Vakspecialist.AanpassenFailedResult.append(self.achievedResult)
        elif self.karakter == 'instabiliteit':
            Vakspecialist.InstabiliteitList.append([self.averageResult, self.achievedResult, self.passed])
            Vakspecialist.InstabiliteitAverageResult.append(self.averageResult)
            Vakspecialist.InstabiliteitAchievedResult.append(self.achievedResult)
            # passed formula
            if self.passed == 'Yes':
                Vakspecialist.InstabiliteitPassedResult.append(self.achievedResult)
            else:
                Vakspecialist.InstabiliteitFailedResult.append(self.achievedResult)
        elif self.karakter == 'conscientieusheid':
            Vakspecialist.ConscientieusheidList.append([self.averageResult, self.achievedResult, self.passed])
            Vakspecialist.ConscientieusheidAverageResult.append(self.averageResult)
            Vakspecialist.ConscientieusheidAchievedResult.append(self.achievedResult)
            # passed formula
            if self.passed == 'Yes':
                Vakspecialist.ConscientieusheidPassedResult.append(self.achievedResult)
            else:
                Vakspecialist.ConscientieusheidFailedResult.append(self.achievedResult)

    def wipeVakspecialistResults(self):
        Vakspecialist.ExtraversieList = []
        Vakspecialist.ExtraversieAverageResult = []
        Vakspecialist.ExtraversieAchievedResult = []
        Vakspecialist.ExtraversiePassedResult = []
        Vakspecialist.ExtraversieFailedResult = []

        Vakspecialist.OpenstaanList = []
        Vakspecialist.OpenstaanAverageResult = []
        Vakspecialist.OpenstaanAchievedResult = []
        Vakspecialist.OpenstaanPassedResult = []
        Vakspecialist.OpenstaanFailedResult = []

        Vakspecialist.AanpassenList = []
        Vakspecialist.AanpassenAverageResult = []
        Vakspecialist.AanpassenAchievedResult = []
        Vakspecialist.AanpassenPassedResult = []
        Vakspecialist.AanpassenFailedResult = []

        Vakspecialist.InstabiliteitList = []
        Vakspecialist.InstabiliteitAverageResult = []
        Vakspecialist.InstabiliteitAchievedResult = []
        Vakspecialist.InstabiliteitPassedResult = []
        Vakspecialist.InstabiliteitFailedResult = []

        Vakspecialist.ConscientieusheidList = []
        Vakspecialist.ConscientieusheidAverageResult = []
        Vakspecialist.ConscientieusheidAchievedResult = []
        Vakspecialist. ConscientieusheidPassedResult = []
        Vakspecialist.ConscientieusheidFailedResult = []

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