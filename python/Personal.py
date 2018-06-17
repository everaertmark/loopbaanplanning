import python.PersonalFolder.Extraversie as Extraversie
import python.PersonalFolder.Openstaan as Openstaan
import python.PersonalFolder.Instabiliteit as Instabiliteit
import python.PersonalFolder.Aanpassen as Aanpassen
import python.PersonalFolder.Conscientieusheid as Conscientieusheid
import python.Query as Query

class Personal:

    #DEFINE PUBLIC FIELDS
    trainingData = []
    userList = []
    characterTraitList = []
    averageResultList = []
    achievedResultList = []
    passedResultList = []
    currentUserId = ''

    #DEFINE Frequency variables
    extraversiePassed = 0
    extraversieFailed = 0
    extraversieSum = 0

    openstaanPassed = 0
    openstaanFailed = 0
    openstaanSum = 0

    instabiliteitPassed = 0
    instabiliteitFailed = 0
    instabiliteitSum = 0

    conscientieusheidPassed = 0
    conscientieusheidFailed = 0
    conscientieusheidSum = 0

    aanpassenPassed = 0
    aanpassenFailed = 0
    aanpassenSum = 0

    #Contructor
    def __init__(self, userId, characterTrait, averageResult, achievedResult, passed):
        #instance variables
        self.userId = userId
        self.characterTrait = characterTrait.strip()
        self.averageResult = averageResult
        self.achievedResult = achievedResult
        self.passed = passed.strip()

        # class variables
        Personal.userList.append(self.userId)
        Personal.characterTraitList.append(self.characterTrait)
        Personal.averageResultList.append(self.averageResult)
        Personal.achievedResultList.append(self.achievedResult)
        Personal.passedResultList.append(self.passed)

        if self.characterTrait == "Extraversie":
            Extraversie.Extraversie(self.userId, self.averageResult, self.achievedResult, self.passed)
        elif self.characterTrait == 'Openstaan':
            Openstaan.Openstaan(self.userId, self.averageResult, self.achievedResult, self.passed)
        elif self.characterTrait == 'Instabiliteit':
            Instabiliteit.Instabiliteit(self.userId, self.averageResult, self.achievedResult, self.passed)
        elif self.characterTrait == 'Aanpassen':
            Aanpassen.Aanpassen(self.userId, self.averageResult, self.achievedResult, self.passed)
        else:
            Conscientieusheid.Conscientieusheid(self.userId, self.averageResult, self.achievedResult, self.passed)

    def wipePersonalRecords(self):
        Personal.extraversiePassed = 0
        Personal.extraversieFailed = 0
        Personal.extraversieSum = 0
        Personal.openstaanPassed = 0
        Personal.openstaanFailed = 0
        Personal.openstaanSum = 0
        Personal.aanpassenPassed = 0
        Personal.aanpassenFailed = 0
        Personal.aanpassenSum = 0
        Personal.instabiliteitPassed = 0
        Personal.instabiliteitFailed = 0
        Personal.instabiliteitSum = 0
        Personal.conscientieusheidPassed = 0
        Personal.conscientieusheidFailed = 0
        Personal.conscientieusheidSum = 0

    def loadGeneralFrequencyTable(self):
        Personal.extraversiePassed = len(Extraversie.Extraversie.getExtraversiePassedResult(Extraversie.Extraversie))
        Personal.extraversieFailed = len(Extraversie.Extraversie.getExtraversieFailedResult(Extraversie.Extraversie))
        Personal.extraversieSum = Personal.extraversiePassed + Personal.extraversieFailed

        Personal.openstaanPassed = len(Openstaan.Openstaan.getOpenstaanPassedResult(Openstaan.Openstaan))
        Personal.openstaanFailed = len(Openstaan.Openstaan.getOpenstaanFailedResult(Openstaan.Openstaan))
        Personal.openstaanSum = Personal.openstaanPassed + Personal.openstaanFailed

        Personal.instabiliteitPassed = len(Instabiliteit.Instabiliteit.getInstabiliteitPassedResult(Instabiliteit.Instabiliteit))
        Personal.instabiliteitFailed = len(Instabiliteit.Instabiliteit.getInstabiliteitFailedResult(Instabiliteit.Instabiliteit))
        Personal.instabiliteitSum = Personal.instabiliteitPassed + Personal.instabiliteitFailed

        Personal.conscientieusheidPassed = len(Conscientieusheid.Conscientieusheid.getConscientieusheidPassedResult(Conscientieusheid.Conscientieusheid))
        Personal.conscientieusheidFailed = len(Conscientieusheid.Conscientieusheid.getConscientieusheidFailedResult(Conscientieusheid.Conscientieusheid))
        Personal.conscientieusheidSum = Personal.conscientieusheidPassed + Personal.conscientieusheidFailed

        Personal.aanpassenPassed = len(Aanpassen.Aanpassen.getAanpassenPassedResult(Aanpassen.Aanpassen))
        Personal.aanpassenFailed = len(Aanpassen.Aanpassen.getAanpassenFailedResult(Aanpassen.Aanpassen))
        Personal.aanpassenSum = Personal.aanpassenPassed + Personal.aanpassenFailed

    def getUserList(self):
        return self.userList

    def getCharacterTraitList(self):
        return self.characterTraitList

    def getAverageResultList(self):
        return self.averageResultList

    def getAchievedResultList(self):
        return self.achievedResultList

    def getPassedResultList(self):
        return self.passedResultList

    def getAanpassenResultList(self):
        return Aanpassen.Aanpassen.getAanpassenList(Aanpassen.Aanpassen)

    def getExtraversieResultList(self):
        return Extraversie.Extraversie.getExtraversieList(Extraversie.Extraversie)

    def getConscientieusheidResultList(self):
        return Conscientieusheid.Conscientieusheid.getConscientieusheidList(Conscientieusheid.Conscientieusheid)

    def getInstabiliteitResultList(self):
        return Instabiliteit.Instabiliteit.getInstabiliteitList(Instabiliteit.Instabiliteit)
    
    def getOpenstaanResultList(self):
        return Openstaan.Openstaan.getOpenstaanList(Openstaan.Openstaan)