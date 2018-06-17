import python.Role.RoleFrequency as RoleFrequency
import pandas as pandas

class Query:

    #Global datset lists
    datasetBPI = pandas.core.frame.DataFrame
    datasetPersonal = pandas.core.frame.DataFrame

    loopbaanRoles = []
    loopbaanLevels = []
    loopbaanYears = []
    loopbaanLevelRoleNames = []

    # Contructor
    def __init__(self, dataset_bpi, dataset_personal):
        Query.datasetBPI = dataset_bpi
        Query.datasetPersonal = dataset_personal

    def getPersonalResultsOfUser(self, userId):
        userListResult = []
        for index, row in Query.datasetPersonal.iterrows():
            if row[0] == userId:
                userListResult.append(row)
            else:
                continue
        return userListResult

    def getBPIResultsOfUser(self, userId):
        BPIResults = []
        for index, row in Query.datasetBPI.iterrows():
            if row[0] == userId:
                BPIResults.append(row)
            else:
                continue
        return BPIResults


    def getRoleOfUser(self, userId):
        userLevel = 0
        for index, row in Query.datasetBPI.iterrows():
            if row[0] == userId:
                userLevel = row[3]
            else:
                continue
        return userLevel

    def getSimilarRoleAndLevelResults(self, role, level):
        similarRoleAndLevel = []
        role = int(role)
        level = int(level)

        for index, row in Query.datasetBPI.iterrows():
            if row[3] == role and row[4] == level:
                similarRoleAndLevel.append(row)
            else:
                continue
        return similarRoleAndLevel

    def getSimilarBPIResults(self, getSimilarRoleAndLevelResults, minimum, maximum):
        similarBPI = []

        for row in getSimilarRoleAndLevelResults:
            if row[6] >= minimum and row[6] <= maximum:
                similarBPI.append(row)
            else:
                continue
        return similarBPI

    def getUserResults(self, similarBPIResults):
        userResults = []
        userIdList = []
        for row in similarBPIResults:
            if row[0] in userIdList:
                continue
            else:
                userIdList.append(row[0])
                userResults.append(row)

        return userResults

    def getLoopbaanPlanningResults(self, similarBPIResults):
        loopbaanplanning = []
        for row in similarBPIResults:
            loopbaanplanning.append(self.getBPIResultsOfUser(self, row[0]))

        return loopbaanplanning

    def getLatestYear(self, resultList):
        latest_year = 1
        for row in resultList:
            if int(row['year']) > latest_year: latest_year = int(row['year'])

        return latest_year

    def generateExtraversieLikeihoodTable(self):
        extraversieTable = []

        # Retrieve the overall results
        overallPassedSum = RoleFrequency.RoleFrequency.assistantPassed + RoleFrequency.RoleFrequency.generalworkerPassed + RoleFrequency.RoleFrequency.allrounderPassed + RoleFrequency.RoleFrequency.vakspecialistPassed
        overallFailedSum = RoleFrequency.RoleFrequency.assistantFailed + RoleFrequency.RoleFrequency.generalworkerFailed + RoleFrequency.RoleFrequency.allrounderFailed + RoleFrequency.RoleFrequency.vakspecialistFailed
        overallSum = overallPassedSum + overallFailedSum
        PassedCalculation = round(overallPassedSum / overallSum, 2)
        FailedCalculation = round(overallFailedSum / overallSum, 2)

        if overallPassedSum > overallFailedSum:
            extravertMorePassed = "extravertMorePassed"
        else:
            extravertMorePassed = "extravertMoreFailed"

        # Generate a top level dataset
        overallResults = {}
        overallResults['extravertPassedSum'] = overallPassedSum
        overallResults['extravertFailedSum'] = overallFailedSum
        overallResults['extravertSum'] = overallSum
        overallResults['extravertpassedCalculation'] = PassedCalculation
        overallResults['extravertfailedCalculation'] = FailedCalculation
        overallResults['extravertMorePassed'] = extravertMorePassed
        # append it to extraversieTable
        extraversieTable.append(overallResults)

        # Generate the sub level datasets
        subResults = []

        AssistantPassedCalc = round(RoleFrequency.RoleFrequency.assistantPassed / overallPassedSum, 2)
        AssistantAmountCalc = round(RoleFrequency.RoleFrequency.assistantSum / overallPassedSum, 2)
        AssistantFinalProb = round((AssistantPassedCalc * PassedCalculation) / AssistantAmountCalc, 2)

        AssistantResults = {}
        AssistantResults['AssistantPassedCalc'] = AssistantPassedCalc
        AssistantResults['AssistantPassed'] = RoleFrequency.RoleFrequency.assistantPassed
        AssistantResults['AssistantFailed'] = RoleFrequency.RoleFrequency.assistantFailed
        AssistantResults['AssistantProb'] = round((100 / RoleFrequency.RoleFrequency.assistantSum) * RoleFrequency.RoleFrequency.assistantPassed, 2)
        AssistantResults['AssistantTotal'] = RoleFrequency.RoleFrequency.assistantPassed + RoleFrequency.RoleFrequency.assistantFailed
        AssistantResults['AssistantAmountCalc'] = AssistantAmountCalc
        AssistantResults['AssistantFinalProb'] = AssistantFinalProb
        subResults.append(AssistantResults)

        GeneralWorkerPassedCalc = round(RoleFrequency.RoleFrequency.generalworkerPassed / overallPassedSum, 2)
        GeneralWorkerAmountCalc = round(RoleFrequency.RoleFrequency.generalworkerSum / overallPassedSum, 2)
        GeneralWorkerFinalProb = round((GeneralWorkerPassedCalc * PassedCalculation) / GeneralWorkerAmountCalc, 2)

        GeneralWorkerResults = {}
        GeneralWorkerResults['GeneralWorkerPassedCalc'] = GeneralWorkerPassedCalc
        GeneralWorkerResults['GeneralWorkerPassed'] = RoleFrequency.RoleFrequency.generalworkerPassed
        GeneralWorkerResults['GeneralWorkerFailed'] = RoleFrequency.RoleFrequency.generalworkerFailed
        GeneralWorkerResults['GeneralWorkerProb'] = round((100 / RoleFrequency.RoleFrequency.generalworkerSum) * RoleFrequency.RoleFrequency.generalworkerPassed, 2)
        GeneralWorkerResults['GeneralWorkerTotal'] = RoleFrequency.RoleFrequency.generalworkerPassed + RoleFrequency.RoleFrequency.generalworkerFailed
        GeneralWorkerResults['GeneralWorkerAmountCalc'] = GeneralWorkerAmountCalc
        GeneralWorkerResults['GeneralWorkerFinalProb'] = GeneralWorkerFinalProb
        subResults.append(GeneralWorkerResults)

        AllRounderPassedCalc = round(RoleFrequency.RoleFrequency.allrounderPassed / overallPassedSum, 2)
        AllRounderAmountCalc = round(RoleFrequency.RoleFrequency.allrounderSum / overallPassedSum, 2)
        AllRounderFinalProb = round((AllRounderPassedCalc * PassedCalculation) / AllRounderAmountCalc, 2)

        AllRounderResults = {}
        AllRounderResults['AllRounderPassedCalc'] = AllRounderPassedCalc
        AllRounderResults['AllRounderPassed'] = RoleFrequency.RoleFrequency.allrounderPassed
        AllRounderResults['AllRounderFailed'] = RoleFrequency.RoleFrequency.allrounderFailed
        AllRounderResults['AllRounderProb'] = round((100 / RoleFrequency.RoleFrequency.allrounderSum) * RoleFrequency.RoleFrequency.allrounderPassed, 2)
        AllRounderResults['AllRounderTotal'] = RoleFrequency.RoleFrequency.allrounderPassed + RoleFrequency.RoleFrequency.allrounderFailed
        AllRounderResults['AllRounderAmountCalc'] = AllRounderAmountCalc
        AllRounderResults['AllRounderFinalProb'] = AllRounderFinalProb
        subResults.append(AllRounderResults)

        VakspecialistPassedCalc = round(RoleFrequency.RoleFrequency.vakspecialistPassed / overallPassedSum, 2)
        VakspecialistAmountCalc = round(RoleFrequency.RoleFrequency.vakspecialistSum / overallPassedSum, 2)
        VakspecialistFinalProb = round((VakspecialistPassedCalc * PassedCalculation) / VakspecialistAmountCalc, 2)

        VakspecialistResults = {}
        VakspecialistResults['VakspecialistPassedCalc'] = VakspecialistPassedCalc
        VakspecialistResults['VakspecialistPassed'] = RoleFrequency.RoleFrequency.vakspecialistPassed
        VakspecialistResults['VakspecialistFailed'] = RoleFrequency.RoleFrequency.vakspecialistFailed
        VakspecialistResults['VakspecialistProb'] = round((100 / RoleFrequency.RoleFrequency.vakspecialistSum) * RoleFrequency.RoleFrequency.vakspecialistPassed, 2)
        VakspecialistResults['VakspecialistTotal'] = RoleFrequency.RoleFrequency.vakspecialistPassed + RoleFrequency.RoleFrequency.vakspecialistFailed
        VakspecialistResults['VakspecialistAmountCalc'] = VakspecialistAmountCalc
        VakspecialistResults['VakspecialistFinalProb'] = VakspecialistFinalProb
        subResults.append(VakspecialistResults)

        extraversieTable.append(subResults)

        return extraversieTable

    def generateOpenstaanLikeihoodTable(self):
        openstaanTable = []

        # Retrieve the overall results
        overallPassedSum = RoleFrequency.RoleFrequency.assistantPassed + RoleFrequency.RoleFrequency.generalworkerPassed + RoleFrequency.RoleFrequency.allrounderPassed + RoleFrequency.RoleFrequency.vakspecialistPassed
        overallFailedSum = RoleFrequency.RoleFrequency.assistantFailed + RoleFrequency.RoleFrequency.generalworkerFailed + RoleFrequency.RoleFrequency.allrounderFailed + RoleFrequency.RoleFrequency.vakspecialistFailed
        overallSum = overallPassedSum + overallFailedSum
        PassedCalculation = round(overallPassedSum / overallSum, 2)
        FailedCalculation = round(overallFailedSum / overallSum, 2)

        if overallPassedSum > overallFailedSum:
            openstaanMorePassed = "openstaanMorePassed"
        else:
            openstaanMorePassed = "openstaanMoreFailed"

        # Generate a top level dataset
        overallResults = {}
        overallResults['openstaanPassedSum'] = overallPassedSum
        overallResults['openstaanFailedSum'] = overallFailedSum
        overallResults['openstaanSum'] = overallSum
        overallResults['openstaanpassedCalculation'] = PassedCalculation
        overallResults['openstaanfailedCalculation'] = FailedCalculation
        overallResults['openstaanMorePassed'] = openstaanMorePassed
        # append it to openstaanTable
        openstaanTable.append(overallResults)

        # Generate the sub level datasets
        subResults = []

        AssistantPassedCalc = round(RoleFrequency.RoleFrequency.assistantPassed / overallPassedSum, 2)
        AssistantAmountCalc = round(RoleFrequency.RoleFrequency.assistantSum / overallPassedSum, 2)
        AssistantFinalProb = round((AssistantPassedCalc * PassedCalculation) / AssistantAmountCalc, 2)

        AssistantResults = {}
        AssistantResults['AssistantPassedCalc'] = AssistantPassedCalc
        AssistantResults['AssistantPassed'] = RoleFrequency.RoleFrequency.assistantPassed
        AssistantResults['AssistantFailed'] = RoleFrequency.RoleFrequency.assistantFailed
        AssistantResults['AssistantProb'] = round((100 / RoleFrequency.RoleFrequency.assistantSum) * RoleFrequency.RoleFrequency.assistantPassed, 2)
        AssistantResults['AssistantTotal'] = RoleFrequency.RoleFrequency.assistantPassed + RoleFrequency.RoleFrequency.assistantFailed
        AssistantResults['AssistantAmountCalc'] = AssistantAmountCalc
        AssistantResults['AssistantFinalProb'] = AssistantFinalProb
        subResults.append(AssistantResults)

        GeneralWorkerPassedCalc = round(RoleFrequency.RoleFrequency.generalworkerPassed / overallPassedSum, 2)
        GeneralWorkerAmountCalc = round(RoleFrequency.RoleFrequency.generalworkerSum / overallPassedSum, 2)
        GeneralWorkerFinalProb = round((GeneralWorkerPassedCalc * PassedCalculation) / GeneralWorkerAmountCalc, 2)

        GeneralWorkerResults = {}
        GeneralWorkerResults['GeneralWorkerPassedCalc'] = GeneralWorkerPassedCalc
        GeneralWorkerResults['GeneralWorkerPassed'] = RoleFrequency.RoleFrequency.generalworkerPassed
        GeneralWorkerResults['GeneralWorkerFailed'] = RoleFrequency.RoleFrequency.generalworkerFailed
        GeneralWorkerResults['GeneralWorkerProb'] = round((100 / RoleFrequency.RoleFrequency.generalworkerSum) * RoleFrequency.RoleFrequency.generalworkerPassed, 2)
        GeneralWorkerResults['GeneralWorkerTotal'] = RoleFrequency.RoleFrequency.generalworkerPassed + RoleFrequency.RoleFrequency.generalworkerFailed
        GeneralWorkerResults['GeneralWorkerAmountCalc'] = GeneralWorkerAmountCalc
        GeneralWorkerResults['GeneralWorkerFinalProb'] = GeneralWorkerFinalProb
        subResults.append(GeneralWorkerResults)

        AllRounderPassedCalc = round(RoleFrequency.RoleFrequency.allrounderPassed / overallPassedSum, 2)
        AllRounderAmountCalc = round(RoleFrequency.RoleFrequency.allrounderSum / overallPassedSum, 2)
        AllRounderFinalProb = round((AllRounderPassedCalc * PassedCalculation) / AllRounderAmountCalc, 2)

        AllRounderResults = {}
        AllRounderResults['AllRounderPassedCalc'] = AllRounderPassedCalc
        AllRounderResults['AllRounderPassed'] = RoleFrequency.RoleFrequency.allrounderPassed
        AllRounderResults['AllRounderFailed'] = RoleFrequency.RoleFrequency.allrounderFailed
        AllRounderResults['AllRounderProb'] = round((100 / RoleFrequency.RoleFrequency.allrounderSum) * RoleFrequency.RoleFrequency.allrounderPassed, 2)
        AllRounderResults['AllRounderTotal'] = RoleFrequency.RoleFrequency.allrounderPassed + RoleFrequency.RoleFrequency.allrounderFailed
        AllRounderResults['AllRounderAmountCalc'] = AllRounderAmountCalc
        AllRounderResults['AllRounderFinalProb'] = AllRounderFinalProb
        subResults.append(AllRounderResults)

        AllRounderPassedCalc = round(RoleFrequency.RoleFrequency.allrounderPassed / overallPassedSum, 2)
        AllRounderAmountCalc = round(RoleFrequency.RoleFrequency.allrounderSum / overallPassedSum, 2)
        AllRounderFinalProb = round((AllRounderPassedCalc * PassedCalculation) / AllRounderAmountCalc, 2)

        AllRounderResults = {}
        AllRounderResults['AllRounderPassedCalc'] = AllRounderPassedCalc
        AllRounderResults['AllRounderPassed'] = RoleFrequency.RoleFrequency.allrounderPassed
        AllRounderResults['AllRounderFailed'] = RoleFrequency.RoleFrequency.allrounderFailed
        AllRounderResults['AllRounderProb'] = round((100 / RoleFrequency.RoleFrequency.allrounderSum) * RoleFrequency.RoleFrequency.allrounderPassed, 2)
        AllRounderResults['AllRounderTotal'] = RoleFrequency.RoleFrequency.allrounderPassed + RoleFrequency.RoleFrequency.allrounderFailed
        AllRounderResults['AllRounderAmountCalc'] = AllRounderAmountCalc
        AllRounderResults['AllRounderFinalProb'] = AllRounderFinalProb
        subResults.append(AllRounderResults)

        VakspecialistPassedCalc = round(RoleFrequency.RoleFrequency.vakspecialistPassed / overallPassedSum, 2)
        VakspecialistAmountCalc = round(RoleFrequency.RoleFrequency.vakspecialistSum / overallPassedSum, 2)
        VakspecialistFinalProb = round((VakspecialistPassedCalc * PassedCalculation) / VakspecialistAmountCalc, 2)

        VakspecialistResults = {}
        VakspecialistResults['VakspecialistPassedCalc'] = VakspecialistPassedCalc
        VakspecialistResults['VakspecialistPassed'] = RoleFrequency.RoleFrequency.vakspecialistPassed
        VakspecialistResults['VakspecialistFailed'] = RoleFrequency.RoleFrequency.vakspecialistFailed
        VakspecialistResults['VakspecialistProb'] = round((100 / RoleFrequency.RoleFrequency.vakspecialistSum) * RoleFrequency.RoleFrequency.vakspecialistPassed, 2)
        VakspecialistResults['VakspecialistTotal'] = RoleFrequency.RoleFrequency.vakspecialistPassed + RoleFrequency.RoleFrequency.vakspecialistFailed
        VakspecialistResults['VakspecialistAmountCalc'] = VakspecialistAmountCalc
        VakspecialistResults['VakspecialistFinalProb'] = VakspecialistFinalProb
        subResults.append(VakspecialistResults)

        openstaanTable.append(subResults)

        return openstaanTable

    def generateAanpassenLikeihoodTable(self):
        aanpassenTable = []

        # Retrieve the overall results
        overallPassedSum = RoleFrequency.RoleFrequency.assistantPassed + RoleFrequency.RoleFrequency.generalworkerPassed + RoleFrequency.RoleFrequency.allrounderPassed + RoleFrequency.RoleFrequency.vakspecialistPassed
        overallFailedSum = RoleFrequency.RoleFrequency.assistantFailed + RoleFrequency.RoleFrequency.generalworkerFailed + RoleFrequency.RoleFrequency.allrounderFailed + RoleFrequency.RoleFrequency.vakspecialistFailed
        overallSum = overallPassedSum + overallFailedSum
        PassedCalculation = round(overallPassedSum / overallSum, 2)
        FailedCalculation = round(overallFailedSum / overallSum, 2)

        if overallPassedSum > overallFailedSum:
            aanpassenMorePassed = "aanpassenMorePassed"
        else:
            aanpassenMorePassed = "aanpassenMoreFailed"

        # Generate a top level dataset
        overallResults = {}
        overallResults['aanpassenPassedSum'] = overallPassedSum
        overallResults['aanpassenFailedSum'] = overallFailedSum
        overallResults['aanpassenSum'] = overallSum
        overallResults['aanpassenpassedCalculation'] = PassedCalculation
        overallResults['aanpassenfailedCalculation'] = FailedCalculation
        overallResults['aanpassenMorePassed'] = aanpassenMorePassed
        # append it to aanpassenTable
        aanpassenTable.append(overallResults)

        # Generate the sub level datasets
        subResults = []

        AssistantPassedCalc = round(RoleFrequency.RoleFrequency.assistantPassed / overallPassedSum, 2)
        AssistantAmountCalc = round(RoleFrequency.RoleFrequency.assistantSum / overallPassedSum, 2)
        AssistantFinalProb = round((AssistantPassedCalc * PassedCalculation) / AssistantAmountCalc, 2)

        AssistantResults = {}
        AssistantResults['AssistantPassedCalc'] = AssistantPassedCalc
        AssistantResults['AssistantPassed'] = RoleFrequency.RoleFrequency.assistantPassed
        AssistantResults['AssistantFailed'] = RoleFrequency.RoleFrequency.assistantFailed
        AssistantResults['AssistantProb'] = round((100 / RoleFrequency.RoleFrequency.assistantSum) * RoleFrequency.RoleFrequency.assistantPassed, 2)
        AssistantResults['AssistantTotal'] = RoleFrequency.RoleFrequency.assistantPassed + RoleFrequency.RoleFrequency.assistantFailed
        AssistantResults['AssistantAmountCalc'] = AssistantAmountCalc
        AssistantResults['AssistantFinalProb'] = AssistantFinalProb
        subResults.append(AssistantResults)

        GeneralWorkerPassedCalc = round(RoleFrequency.RoleFrequency.generalworkerPassed / overallPassedSum, 2)
        GeneralWorkerAmountCalc = round(RoleFrequency.RoleFrequency.generalworkerSum / overallPassedSum, 2)
        GeneralWorkerFinalProb = round((GeneralWorkerPassedCalc * PassedCalculation) / GeneralWorkerAmountCalc, 2)

        GeneralWorkerResults = {}
        GeneralWorkerResults['GeneralWorkerPassedCalc'] = GeneralWorkerPassedCalc
        GeneralWorkerResults['GeneralWorkerPassed'] = RoleFrequency.RoleFrequency.generalworkerPassed
        GeneralWorkerResults['GeneralWorkerFailed'] = RoleFrequency.RoleFrequency.generalworkerFailed
        GeneralWorkerResults['GeneralWorkerProb'] = round((100 / RoleFrequency.RoleFrequency.generalworkerSum) * RoleFrequency.RoleFrequency.generalworkerPassed, 2)
        GeneralWorkerResults['GeneralWorkerTotal'] = RoleFrequency.RoleFrequency.generalworkerPassed + RoleFrequency.RoleFrequency.generalworkerFailed
        GeneralWorkerResults['GeneralWorkerAmountCalc'] = GeneralWorkerAmountCalc
        GeneralWorkerResults['GeneralWorkerFinalProb'] = GeneralWorkerFinalProb
        subResults.append(GeneralWorkerResults)

        AllRounderPassedCalc = round(RoleFrequency.RoleFrequency.allrounderPassed / overallPassedSum, 2)
        AllRounderAmountCalc = round(RoleFrequency.RoleFrequency.allrounderSum / overallPassedSum, 2)
        AllRounderFinalProb = round((AllRounderPassedCalc * PassedCalculation) / AllRounderAmountCalc, 2)

        AllRounderResults = {}
        AllRounderResults['AllRounderPassedCalc'] = AllRounderPassedCalc
        AllRounderResults['AllRounderPassed'] = RoleFrequency.RoleFrequency.allrounderPassed
        AllRounderResults['AllRounderFailed'] = RoleFrequency.RoleFrequency.allrounderFailed
        AllRounderResults['AllRounderProb'] = round((100 / RoleFrequency.RoleFrequency.allrounderSum) * RoleFrequency.RoleFrequency.allrounderPassed, 2)
        AllRounderResults['AllRounderTotal'] = RoleFrequency.RoleFrequency.allrounderPassed + RoleFrequency.RoleFrequency.allrounderFailed
        AllRounderResults['AllRounderAmountCalc'] = AllRounderAmountCalc
        AllRounderResults['AllRounderFinalProb'] = AllRounderFinalProb
        subResults.append(AllRounderResults)

        VakspecialistPassedCalc = round(RoleFrequency.RoleFrequency.vakspecialistPassed / overallPassedSum, 2)
        VakspecialistAmountCalc = round(RoleFrequency.RoleFrequency.vakspecialistSum / overallPassedSum, 2)
        VakspecialistFinalProb = round((VakspecialistPassedCalc * PassedCalculation) / VakspecialistAmountCalc, 2)

        VakspecialistResults = {}
        VakspecialistResults['VakspecialistPassedCalc'] = VakspecialistPassedCalc
        VakspecialistResults['VakspecialistPassed'] = RoleFrequency.RoleFrequency.vakspecialistPassed
        VakspecialistResults['VakspecialistFailed'] = RoleFrequency.RoleFrequency.vakspecialistFailed
        VakspecialistResults['VakspecialistProb'] = round((100 / RoleFrequency.RoleFrequency.vakspecialistSum) * RoleFrequency.RoleFrequency.vakspecialistPassed, 2)
        VakspecialistResults['VakspecialistTotal'] = RoleFrequency.RoleFrequency.vakspecialistPassed + RoleFrequency.RoleFrequency.vakspecialistFailed
        VakspecialistResults['VakspecialistAmountCalc'] = VakspecialistAmountCalc
        VakspecialistResults['VakspecialistFinalProb'] = VakspecialistFinalProb
        subResults.append(VakspecialistResults)

        aanpassenTable.append(subResults)

        return aanpassenTable

    def generateInstabiliteitLikeihoodTable(self):
        instabiliteitTable = []

        # Retrieve the overall results
        overallPassedSum = RoleFrequency.RoleFrequency.assistantPassed + RoleFrequency.RoleFrequency.generalworkerPassed + RoleFrequency.RoleFrequency.allrounderPassed + RoleFrequency.RoleFrequency.vakspecialistPassed
        overallFailedSum = RoleFrequency.RoleFrequency.assistantFailed + RoleFrequency.RoleFrequency.generalworkerFailed + RoleFrequency.RoleFrequency.allrounderFailed + RoleFrequency.RoleFrequency.vakspecialistFailed
        overallSum = overallPassedSum + overallFailedSum
        PassedCalculation = round(overallPassedSum / overallSum, 2)
        FailedCalculation = round(overallFailedSum / overallSum, 2)

        if overallPassedSum > overallFailedSum:
            instabiliteitMorePassed = "instabiliteitMorePassed"
        else:
            instabiliteitMorePassed = "instabiliteitMoreFailed"

        # Generate a top level dataset
        overallResults = {}
        overallResults['instabiliteitPassedSum'] = overallPassedSum
        overallResults['instabiliteitFailedSum'] = overallFailedSum
        overallResults['instabiliteitSum'] = overallSum
        overallResults['instabiliteitpassedCalculation'] = PassedCalculation
        overallResults['instabiliteitfailedCalculation'] = FailedCalculation
        overallResults['instabiliteitMorePassed'] = instabiliteitMorePassed
        # append it to instabiliteitTable
        instabiliteitTable.append(overallResults)

        # Generate the sub level datasets
        subResults = []

        AssistantPassedCalc = round(RoleFrequency.RoleFrequency.assistantPassed / overallPassedSum, 2)
        AssistantAmountCalc = round(RoleFrequency.RoleFrequency.assistantSum / overallPassedSum, 2)
        AssistantFinalProb = round((AssistantPassedCalc * PassedCalculation) / AssistantAmountCalc, 2)

        AssistantResults = {}
        AssistantResults['AssistantPassedCalc'] = AssistantPassedCalc
        AssistantResults['AssistantPassed'] = RoleFrequency.RoleFrequency.assistantPassed
        AssistantResults['AssistantFailed'] = RoleFrequency.RoleFrequency.assistantFailed
        AssistantResults['AssistantProb'] = round((100 / RoleFrequency.RoleFrequency.assistantSum) * RoleFrequency.RoleFrequency.assistantPassed, 2)
        AssistantResults['AssistantTotal'] = RoleFrequency.RoleFrequency.assistantPassed + RoleFrequency.RoleFrequency.assistantFailed
        AssistantResults['AssistantAmountCalc'] = AssistantAmountCalc
        AssistantResults['AssistantFinalProb'] = AssistantFinalProb
        subResults.append(AssistantResults)

        GeneralWorkerPassedCalc = round(RoleFrequency.RoleFrequency.generalworkerPassed / overallPassedSum, 2)
        GeneralWorkerAmountCalc = round(RoleFrequency.RoleFrequency.generalworkerSum / overallPassedSum, 2)
        GeneralWorkerFinalProb = round((GeneralWorkerPassedCalc * PassedCalculation) / GeneralWorkerAmountCalc, 2)

        GeneralWorkerResults = {}
        GeneralWorkerResults['GeneralWorkerPassedCalc'] = GeneralWorkerPassedCalc
        GeneralWorkerResults['GeneralWorkerPassed'] = RoleFrequency.RoleFrequency.generalworkerPassed
        GeneralWorkerResults['GeneralWorkerFailed'] = RoleFrequency.RoleFrequency.generalworkerFailed
        GeneralWorkerResults['GeneralWorkerProb'] = round((100 / RoleFrequency.RoleFrequency.generalworkerSum) * RoleFrequency.RoleFrequency.generalworkerPassed, 2)
        GeneralWorkerResults['GeneralWorkerTotal'] = RoleFrequency.RoleFrequency.generalworkerPassed + RoleFrequency.RoleFrequency.generalworkerFailed
        GeneralWorkerResults['GeneralWorkerAmountCalc'] = GeneralWorkerAmountCalc
        GeneralWorkerResults['GeneralWorkerFinalProb'] = GeneralWorkerFinalProb
        subResults.append(GeneralWorkerResults)

        AllRounderPassedCalc = round(RoleFrequency.RoleFrequency.allrounderPassed / overallPassedSum, 2)
        AllRounderAmountCalc = round(RoleFrequency.RoleFrequency.allrounderSum / overallPassedSum, 2)
        AllRounderFinalProb = round((AllRounderPassedCalc * PassedCalculation) / AllRounderAmountCalc, 2)

        AllRounderResults = {}
        AllRounderResults['AllRounderPassedCalc'] = AllRounderPassedCalc
        AllRounderResults['AllRounderPassed'] = RoleFrequency.RoleFrequency.allrounderPassed
        AllRounderResults['AllRounderFailed'] = RoleFrequency.RoleFrequency.allrounderFailed
        AllRounderResults['AllRounderProb'] = round((100 / RoleFrequency.RoleFrequency.allrounderSum) * RoleFrequency.RoleFrequency.allrounderPassed, 2)
        AllRounderResults['AllRounderTotal'] = RoleFrequency.RoleFrequency.allrounderPassed + RoleFrequency.RoleFrequency.allrounderFailed
        AllRounderResults['AllRounderAmountCalc'] = AllRounderAmountCalc
        AllRounderResults['AllRounderFinalProb'] = AllRounderFinalProb
        subResults.append(AllRounderResults)

        VakspecialistPassedCalc = round(RoleFrequency.RoleFrequency.vakspecialistPassed / overallPassedSum, 2)
        VakspecialistAmountCalc = round(RoleFrequency.RoleFrequency.vakspecialistSum / overallPassedSum, 2)
        VakspecialistFinalProb = round((VakspecialistPassedCalc * PassedCalculation) / VakspecialistAmountCalc, 2)

        VakspecialistResults = {}
        VakspecialistResults['VakspecialistPassedCalc'] = VakspecialistPassedCalc
        VakspecialistResults['VakspecialistPassed'] = RoleFrequency.RoleFrequency.vakspecialistPassed
        VakspecialistResults['VakspecialistFailed'] = RoleFrequency.RoleFrequency.vakspecialistFailed
        VakspecialistResults['VakspecialistProb'] = round((100 / RoleFrequency.RoleFrequency.vakspecialistSum) * RoleFrequency.RoleFrequency.vakspecialistPassed, 2)
        VakspecialistResults['VakspecialistTotal'] = RoleFrequency.RoleFrequency.vakspecialistPassed + RoleFrequency.RoleFrequency.vakspecialistFailed
        VakspecialistResults['VakspecialistAmountCalc'] = VakspecialistAmountCalc
        VakspecialistResults['VakspecialistFinalProb'] = VakspecialistFinalProb
        subResults.append(VakspecialistResults)

        instabiliteitTable.append(subResults)

        return instabiliteitTable

    def generateConscientieusheidLikeihoodTable(self):
        conscientieusheidTable = []

        # Retrieve the overall results
        overallPassedSum = RoleFrequency.RoleFrequency.assistantPassed + RoleFrequency.RoleFrequency.generalworkerPassed + RoleFrequency.RoleFrequency.allrounderPassed + RoleFrequency.RoleFrequency.vakspecialistPassed
        overallFailedSum = RoleFrequency.RoleFrequency.assistantFailed + RoleFrequency.RoleFrequency.generalworkerFailed + RoleFrequency.RoleFrequency.allrounderFailed + RoleFrequency.RoleFrequency.vakspecialistFailed
        overallSum = overallPassedSum + overallFailedSum
        PassedCalculation = round(overallPassedSum / overallSum, 2)
        FailedCalculation = round(overallFailedSum / overallSum, 2)

        if overallPassedSum > overallFailedSum:
            conscientieusheidMorePassed = "conscientieusheidMorePassed"
        else:
            conscientieusheidMorePassed = "conscientieusheidMoreFailed"

        # Generate a top level dataset
        overallResults = {}
        overallResults['conscientieusheidPassedSum'] = overallPassedSum
        overallResults['conscientieusheidFailedSum'] = overallFailedSum
        overallResults['conscientieusheidSum'] = overallSum
        overallResults['conscientieusheidpassedCalculation'] = PassedCalculation
        overallResults['conscientieusheidfailedCalculation'] = FailedCalculation
        overallResults['conscientieusheidMorePassed'] = conscientieusheidMorePassed
        # append it to conscientieusheidTable
        conscientieusheidTable.append(overallResults)

        # Generate the sub level datasets
        subResults = []

        AssistantPassedCalc = round(RoleFrequency.RoleFrequency.assistantPassed / overallPassedSum, 2)
        AssistantAmountCalc = round(RoleFrequency.RoleFrequency.assistantSum / overallPassedSum, 2)
        AssistantFinalProb = round((AssistantPassedCalc * PassedCalculation) / AssistantAmountCalc, 2)

        AssistantResults = {}
        AssistantResults['AssistantPassedCalc'] = AssistantPassedCalc
        AssistantResults['AssistantPassed'] = RoleFrequency.RoleFrequency.assistantPassed
        AssistantResults['AssistantFailed'] = RoleFrequency.RoleFrequency.assistantFailed
        AssistantResults['AssistantProb'] = round((100 / RoleFrequency.RoleFrequency.assistantSum) * RoleFrequency.RoleFrequency.assistantPassed, 2)
        AssistantResults['AssistantTotal'] = RoleFrequency.RoleFrequency.assistantPassed + RoleFrequency.RoleFrequency.assistantFailed
        AssistantResults['AssistantAmountCalc'] = AssistantAmountCalc
        AssistantResults['AssistantFinalProb'] = AssistantFinalProb
        subResults.append(AssistantResults)

        GeneralWorkerPassedCalc = round(RoleFrequency.RoleFrequency.generalworkerPassed / overallPassedSum, 2)
        GeneralWorkerAmountCalc = round(RoleFrequency.RoleFrequency.generalworkerSum / overallPassedSum, 2)
        GeneralWorkerFinalProb = round((GeneralWorkerPassedCalc * PassedCalculation) / GeneralWorkerAmountCalc, 2)

        GeneralWorkerResults = {}
        GeneralWorkerResults['GeneralWorkerPassedCalc'] = GeneralWorkerPassedCalc
        GeneralWorkerResults['GeneralWorkerPassed'] = RoleFrequency.RoleFrequency.generalworkerPassed
        GeneralWorkerResults['GeneralWorkerFailed'] = RoleFrequency.RoleFrequency.generalworkerFailed
        GeneralWorkerResults['GeneralWorkerProb'] = round((100 / RoleFrequency.RoleFrequency.generalworkerSum) * RoleFrequency.RoleFrequency.generalworkerPassed, 2)
        GeneralWorkerResults['GeneralWorkerTotal'] = RoleFrequency.RoleFrequency.generalworkerPassed + RoleFrequency.RoleFrequency.generalworkerFailed
        GeneralWorkerResults['GeneralWorkerAmountCalc'] = GeneralWorkerAmountCalc
        GeneralWorkerResults['GeneralWorkerFinalProb'] = GeneralWorkerFinalProb
        subResults.append(GeneralWorkerResults)

        AllRounderPassedCalc = round(RoleFrequency.RoleFrequency.allrounderPassed / overallPassedSum, 2)
        AllRounderAmountCalc = round(RoleFrequency.RoleFrequency.allrounderSum / overallPassedSum, 2)
        AllRounderFinalProb = round((AllRounderPassedCalc * PassedCalculation) / AllRounderAmountCalc, 2)

        AllRounderResults = {}
        AllRounderResults['AllRounderPassedCalc'] = AllRounderPassedCalc
        AllRounderResults['AllRounderPassed'] = RoleFrequency.RoleFrequency.allrounderPassed
        AllRounderResults['AllRounderFailed'] = RoleFrequency.RoleFrequency.allrounderFailed
        AllRounderResults['AllRounderProb'] = round((100 / RoleFrequency.RoleFrequency.allrounderSum) * RoleFrequency.RoleFrequency.allrounderPassed, 2)
        AllRounderResults['AllRounderTotal'] = RoleFrequency.RoleFrequency.allrounderPassed + RoleFrequency.RoleFrequency.allrounderFailed
        AllRounderResults['AllRounderAmountCalc'] = AllRounderAmountCalc
        AllRounderResults['AllRounderFinalProb'] = AllRounderFinalProb
        subResults.append(AllRounderResults)

        VakspecialistPassedCalc = round(RoleFrequency.RoleFrequency.vakspecialistPassed / overallPassedSum, 2)
        VakspecialistAmountCalc = round(RoleFrequency.RoleFrequency.vakspecialistSum / overallPassedSum, 2)
        VakspecialistFinalProb = round((VakspecialistPassedCalc * PassedCalculation) / VakspecialistAmountCalc, 2)

        VakspecialistResults = {}
        VakspecialistResults['VakspecialistPassedCalc'] = VakspecialistPassedCalc
        VakspecialistResults['VakspecialistPassed'] = RoleFrequency.RoleFrequency.vakspecialistPassed
        VakspecialistResults['VakspecialistFailed'] = RoleFrequency.RoleFrequency.vakspecialistFailed
        VakspecialistResults['VakspecialistProb'] = round((100 / RoleFrequency.RoleFrequency.vakspecialistSum) * RoleFrequency.RoleFrequency.vakspecialistPassed, 2)
        VakspecialistResults['VakspecialistTotal'] = RoleFrequency.RoleFrequency.vakspecialistPassed + RoleFrequency.RoleFrequency.vakspecialistFailed
        VakspecialistResults['VakspecialistAmountCalc'] = VakspecialistAmountCalc
        VakspecialistResults['VakspecialistFinalProb'] = VakspecialistFinalProb
        subResults.append(VakspecialistResults)

        conscientieusheidTable.append(subResults)

        return conscientieusheidTable