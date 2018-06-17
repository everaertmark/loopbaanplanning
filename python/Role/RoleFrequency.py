import python.Role.Assistant as Assistant
import python.Role.GeneralWorker as GeneralWorker
import python.Role.AllRounder as AllRounder
import python.Role.Vakspecialist as Vakspecialist

class RoleFrequency:

    #DEFINE Variant variables
    assistantBaseScore = 20
    generalWorkerBaseScore = 15
    allrounderBaseScore = 12
    vakspecialistBaseScore = 10

    #DEFINE Frequency variables
    assistantPassed = 0
    assistantFailed = 0
    assistantSum = 0

    generalworkerPassed = 0
    generalworkerFailed = 0
    generalworkerSum = 0

    allrounderPassed = 0
    allrounderFailed = 0
    allrounderSum = 0

    vakspecialistPassed = 0
    vakspecialistFailed = 0
    vakspecialistSum = 0

    def wipeFrequencyVariables(self):
        RoleFrequency.assistantPassed = 0
        RoleFrequency.assistantFailed = 0
        RoleFrequency.assistantSum = 0
        RoleFrequency.generalworkerPassed = 0
        RoleFrequency.generalworkerFailed = 0
        RoleFrequency.generalworkerSum = 0
        RoleFrequency.allrounderPassed = 0
        RoleFrequency.allrounderFailed = 0
        RoleFrequency.allrounderSum = 0
        RoleFrequency.vakspecialistPassed = 0
        RoleFrequency.vakspecialistFailed = 0
        RoleFrequency.vakspecialistSum = 0

    def loadExtraversieFrequencyTable(self):
        RoleFrequency.assistantPassed = len(Assistant.Assistant.getExtraversiePassedResult(Assistant.Assistant))
        RoleFrequency.assistantFailed = len(Assistant.Assistant.getExtraversieFailedResult(Assistant.Assistant))
        RoleFrequency.assistantSum = RoleFrequency.assistantPassed + RoleFrequency.assistantFailed

        RoleFrequency.generalworkerPassed = len(GeneralWorker.GeneralWorker.getExtraversiePassedResult(GeneralWorker.GeneralWorker))
        RoleFrequency.generalworkerFailed = len(GeneralWorker.GeneralWorker.getExtraversieFailedResult(GeneralWorker.GeneralWorker))
        RoleFrequency.generalworkerSum = RoleFrequency.generalworkerPassed + RoleFrequency.generalworkerFailed

        RoleFrequency.allrounderPassed = len(AllRounder.AllRounder.getExtraversiePassedResult(AllRounder.AllRounder))
        RoleFrequency.allrounderFailed = len(AllRounder.AllRounder.getExtraversieFailedResult(AllRounder.AllRounder))
        RoleFrequency.allrounderSum = RoleFrequency.allrounderPassed + RoleFrequency.allrounderFailed

        RoleFrequency.vakspecialistPassed = len(Vakspecialist.Vakspecialist.getExtraversiePassedResult(Vakspecialist.Vakspecialist))
        RoleFrequency.vakspecialistFailed = len(Vakspecialist.Vakspecialist.getExtraversieFailedResult(Vakspecialist.Vakspecialist))
        RoleFrequency.vakspecialistSum = RoleFrequency.vakspecialistPassed + RoleFrequency.vakspecialistFailed

    def loadOpenstaanFrequencyTable(self):
        RoleFrequency.assistantPassed = len(Assistant.Assistant.getOpenstaanPassedResult(Assistant.Assistant))
        RoleFrequency.assistantFailed = len(Assistant.Assistant.getOpenstaanFailedResult(Assistant.Assistant))
        RoleFrequency.assistantSum = RoleFrequency.assistantPassed + RoleFrequency.assistantFailed

        RoleFrequency.generalworkerPassed = len(GeneralWorker.GeneralWorker.getOpenstaanPassedResult(GeneralWorker.GeneralWorker))
        RoleFrequency.generalworkerFailed = len(GeneralWorker.GeneralWorker.getOpenstaanFailedResult(GeneralWorker.GeneralWorker))
        RoleFrequency.generalworkerSum = RoleFrequency.generalworkerPassed + RoleFrequency.generalworkerFailed

        RoleFrequency.allrounderPassed = len(AllRounder.AllRounder.getOpenstaanPassedResult(AllRounder.AllRounder))
        RoleFrequency.allrounderFailed = len(AllRounder.AllRounder.getOpenstaanFailedResult(AllRounder.AllRounder))
        RoleFrequency.allrounderSum = RoleFrequency.allrounderPassed + RoleFrequency.allrounderFailed

        RoleFrequency.vakspecialistPassed = len(Vakspecialist.Vakspecialist.getExtraversiePassedResult(Vakspecialist.Vakspecialist))
        RoleFrequency.vakspecialistFailed = len(Vakspecialist.Vakspecialist.getExtraversieFailedResult(Vakspecialist.Vakspecialist))
        RoleFrequency.vakspecialistSum = RoleFrequency.vakspecialistPassed + RoleFrequency.vakspecialistFailed

    def loadAanpassenFrequencyTable(self):
        RoleFrequency.assistantPassed = len(Assistant.Assistant.getAanpassenPassedResult(Assistant.Assistant))
        RoleFrequency.assistantFailed = len(Assistant.Assistant.getAanpassenFailedResult(Assistant.Assistant))
        RoleFrequency.assistantSum = RoleFrequency.assistantPassed + RoleFrequency.assistantFailed

        RoleFrequency.generalworkerPassed = len(GeneralWorker.GeneralWorker.getAanpassenPassedResult(GeneralWorker.GeneralWorker))
        RoleFrequency.generalworkerFailed = len(GeneralWorker.GeneralWorker.getAanpassenFailedResult(GeneralWorker.GeneralWorker))
        RoleFrequency.generalworkerSum = RoleFrequency.generalworkerPassed + RoleFrequency.generalworkerFailed

        RoleFrequency.allrounderPassed = len(AllRounder.AllRounder.getOpenstaanPassedResult(AllRounder.AllRounder))
        RoleFrequency.allrounderFailed = len(AllRounder.AllRounder.getOpenstaanFailedResult(AllRounder.AllRounder))
        RoleFrequency.allrounderSum = RoleFrequency.allrounderPassed + RoleFrequency.allrounderFailed

        RoleFrequency.vakspecialistPassed = len(Vakspecialist.Vakspecialist.getExtraversiePassedResult(Vakspecialist.Vakspecialist))
        RoleFrequency.vakspecialistFailed = len(Vakspecialist.Vakspecialist.getExtraversieFailedResult(Vakspecialist.Vakspecialist))
        RoleFrequency.vakspecialistSum = RoleFrequency.vakspecialistPassed + RoleFrequency.vakspecialistFailed

    def loadInstabiliteitFrequencyTable(self):
        RoleFrequency.assistantPassed = len(Assistant.Assistant.getInstabiliteitPassedResult(Assistant.Assistant))
        RoleFrequency.assistantFailed = len(Assistant.Assistant.getInstabiliteitFailedResult(Assistant.Assistant))
        RoleFrequency.assistantSum = RoleFrequency.assistantPassed + RoleFrequency.assistantFailed

        RoleFrequency.generalworkerPassed = len(GeneralWorker.GeneralWorker.getInstabiliteitPassedResult(GeneralWorker.GeneralWorker))
        RoleFrequency.generalworkerFailed = len(GeneralWorker.GeneralWorker.getInstabiliteitFailedResult(GeneralWorker.GeneralWorker))
        RoleFrequency.generalworkerSum = RoleFrequency.generalworkerPassed + RoleFrequency.generalworkerFailed

        RoleFrequency.allrounderPassed = len(AllRounder.AllRounder.getInstabiliteitPassedResult(AllRounder.AllRounder))
        RoleFrequency.allrounderFailed = len(AllRounder.AllRounder.getInstabiliteitFailedResult(AllRounder.AllRounder))
        RoleFrequency.allrounderSum = RoleFrequency.allrounderPassed + RoleFrequency.allrounderFailed

        RoleFrequency.vakspecialistPassed = len(Vakspecialist.Vakspecialist.getExtraversiePassedResult(Vakspecialist.Vakspecialist))
        RoleFrequency.vakspecialistFailed = len(Vakspecialist.Vakspecialist.getExtraversieFailedResult(Vakspecialist.Vakspecialist))
        RoleFrequency.vakspecialistSum = RoleFrequency.vakspecialistPassed + RoleFrequency.vakspecialistFailed

    def loadConscientieusheidFrequencyTable(self):
        RoleFrequency.assistantPassed = len(Assistant.Assistant.getConscientieusheidPassedResult(Assistant.Assistant))
        RoleFrequency.assistantFailed = len(Assistant.Assistant.getConscientieusheidFailedResult(Assistant.Assistant))
        RoleFrequency.assistantSum = RoleFrequency.assistantPassed + RoleFrequency.assistantFailed

        RoleFrequency.generalworkerPassed = len(GeneralWorker.GeneralWorker.getConscientieusheidPassedResult(GeneralWorker.GeneralWorker))
        RoleFrequency.generalworkerFailed = len(GeneralWorker.GeneralWorker.getConscientieusheidFailedResult(GeneralWorker.GeneralWorker))
        RoleFrequency.generalworkerSum = RoleFrequency.generalworkerPassed + RoleFrequency.generalworkerFailed

        RoleFrequency.allrounderPassed = len(AllRounder.AllRounder.getConscientieusheidPassedResult(AllRounder.AllRounder))
        RoleFrequency.allrounderFailed = len(AllRounder.AllRounder.getConscientieusheidFailedResult(AllRounder.AllRounder))
        RoleFrequency.allrounderSum = RoleFrequency.allrounderPassed + RoleFrequency.allrounderFailed

        RoleFrequency.vakspecialistPassed = len(Vakspecialist.Vakspecialist.getExtraversiePassedResult(Vakspecialist.Vakspecialist))
        RoleFrequency.vakspecialistFailed = len(Vakspecialist.Vakspecialist.getExtraversieFailedResult(Vakspecialist.Vakspecialist))
        RoleFrequency.vakspecialistSum = RoleFrequency.vakspecialistPassed + RoleFrequency.vakspecialistFailed