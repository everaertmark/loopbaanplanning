class GeneralWorker:

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
            GeneralWorker.ExtraversieList.append([self.averageResult, self.achievedResult, self.passed])
            GeneralWorker.ExtraversieAverageResult.append(self.averageResult)
            GeneralWorker.ExtraversieAchievedResult.append(self.achievedResult)
            # passed formula
            if self.passed == 'Yes':
                GeneralWorker.ExtraversiePassedResult.append(self.achievedResult)
            else:
                GeneralWorker.ExtraversieFailedResult.append(self.achievedResult)
        elif self.karakter == 'openstaan':
            GeneralWorker.OpenstaanList.append([self.averageResult, self.achievedResult, self.passed])
            GeneralWorker.OpenstaanAverageResult.append(self.averageResult)
            GeneralWorker.OpenstaanAchievedResult.append(self.achievedResult)
            # passed formula
            if self.passed == 'Yes':
                GeneralWorker.OpenstaanPassedResult.append(self.achievedResult)
            else:
                GeneralWorker.OpenstaanFailedResult.append(self.achievedResult)
        elif self.karakter == 'aanpassen':
            GeneralWorker.AanpassenList.append([self.averageResult, self.achievedResult, self.passed])
            GeneralWorker.AanpassenAverageResult.append(self.averageResult)
            GeneralWorker.AanpassenAchievedResult.append(self.achievedResult)
            # passed formula
            if self.passed == 'Yes':
                GeneralWorker.AanpassenPassedResult.append(self.achievedResult)
            else:
                GeneralWorker.AanpassenFailedResult.append(self.achievedResult)
        elif self.karakter == 'instabiliteit':
            GeneralWorker.InstabiliteitList.append([self.averageResult, self.achievedResult, self.passed])
            GeneralWorker.InstabiliteitAverageResult.append(self.averageResult)
            GeneralWorker.InstabiliteitAchievedResult.append(self.achievedResult)
            # passed formula
            if self.passed == 'Yes':
                GeneralWorker.InstabiliteitPassedResult.append(self.achievedResult)
            else:
                GeneralWorker.InstabiliteitFailedResult.append(self.achievedResult)
        elif self.karakter == 'conscientieusheid':
            GeneralWorker.ConscientieusheidList.append([self.averageResult, self.achievedResult, self.passed])
            GeneralWorker.ConscientieusheidAverageResult.append(self.averageResult)
            GeneralWorker.ConscientieusheidAchievedResult.append(self.achievedResult)
            # passed formula
            if self.passed == 'Yes':
                GeneralWorker.ConscientieusheidPassedResult.append(self.achievedResult)
            else:
                GeneralWorker.ConscientieusheidFailedResult.append(self.achievedResult)

    def wipeGeneralWorkerResults(self):
        GeneralWorker.ExtraversieList = []
        GeneralWorker.ExtraversieAverageResult = []
        GeneralWorker.ExtraversieAchievedResult = []
        GeneralWorker.ExtraversiePassedResult = []
        GeneralWorker.ExtraversieFailedResult = []

        GeneralWorker.OpenstaanList = []
        GeneralWorker.OpenstaanAverageResult = []
        GeneralWorker.OpenstaanAchievedResult = []
        GeneralWorker.OpenstaanPassedResult = []
        GeneralWorker.OpenstaanFailedResult = []

        GeneralWorker.AanpassenList = []
        GeneralWorker.AanpassenAverageResult = []
        GeneralWorker.AanpassenAchievedResult = []
        GeneralWorker.AanpassenPassedResult = []
        GeneralWorker.AanpassenFailedResult = []

        GeneralWorker.InstabiliteitList = []
        GeneralWorker.InstabiliteitAverageResult = []
        GeneralWorker.InstabiliteitAchievedResult = []
        GeneralWorker.InstabiliteitPassedResult = []
        GeneralWorker.InstabiliteitFailedResult = []

        GeneralWorker.ConscientieusheidList = []
        GeneralWorker.ConscientieusheidAverageResult = []
        GeneralWorker.ConscientieusheidAchievedResult = []
        GeneralWorker. ConscientieusheidPassedResult = []
        GeneralWorker.ConscientieusheidFailedResult = []

    #GeneralWorker methods
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