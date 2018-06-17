import pandas as pandas
import os
import json as json
import python.Personal as Personal
import python.BPI as BPI
import python.GeneralPerson as GeneralPerson
import python.Query as Query
import python.Role.RoleFrequency as RoleFrequency
import python.Role.Assistant as Assistant
import python.Role.GeneralWorker as GeneralWorker
import python.Role.AllRounder as AllRounder
import python.Role.Vakspecialist as Vakspecialist
import python.Variant.extraversieVariant as extraversieVariant
import python.Variant.aanpassenVariant as aanpassenVariant
import python.Variant.openstaanVariant as openstaanVariant
import python.Variant.instabiliteitVariant as instabiliteitVariant
import python.Variant.conscientieusheidVariant as conscientieusheidVariant

#DEFINE TABLE COLUMS
BPI_ATTR_NAMES = ["user_id", "test_id", "function", "role", "level", "average_result", "achieved_result", "year"]
PERSONAL_ATTR_NAMES = ["user_id", "karaktereigenschap", "average_result", "achieved_result", "passed"]
singletonPersonInstance = ""
#FIELD_NAMES = ["Num"] + ATTR_NAMES + ["Class"]

# 1 = Assistant
# 2 = General Worker
# 3 = All-rounder

#DEFINE Global Array
training_data = []

def runMain():
    currentPath = os.path.dirname(os.path.dirname(__file__))
    bpi = "python/bpi.csv"
    personal = "python/personal.csv"

    bpiPath = os.path.join(currentPath, bpi)
    personalPath = os.path.join(currentPath, personal)

    datasetBPI = pandas.read_csv(bpiPath, names=BPI_ATTR_NAMES, delimiter=',')
    datasetPERSONAL = pandas.read_csv(personalPath, names=PERSONAL_ATTR_NAMES, delimiter=',')

    #Save the datasets for future queries
    Query.Query(datasetBPI, datasetPERSONAL)

    Assistant.Assistant.wipeAssistantResults(Assistant.Assistant)
    GeneralWorker.GeneralWorker.wipeGeneralWorkerResults(GeneralWorker.GeneralWorker)
    AllRounder.AllRounder.wipeAllRounderResults(AllRounder.AllRounder)
    Vakspecialist.Vakspecialist.wipeVakspecialistResults(Vakspecialist.Vakspecialist)

    for index, row in datasetPERSONAL.iterrows():
        Personal.Personal(row[0], row[1], row[2], row[3], row[4])

    for index, row in datasetBPI.iterrows():
        BPI.BPI(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])

    # print(Query.Query.getBPIResultsOfUser(Query.Query, "701a216dc42833ea3b702b478a62c031"))

    # //////////////////////////////////////////////////////////////////
    # Generate a general probability factor for each BIG 5 character trait
    Personal.Personal.loadGeneralFrequencyTable(Personal.Personal)
    return GeneralPerson.generateLikeihoodTable()

def runTraitFrequencies():

    #load Frequencylevels for Extraversie
    RoleFrequency.RoleFrequency.loadExtraversieFrequencyTable(RoleFrequency.RoleFrequency)
    extraversie = Query.Query.generateExtraversieLikeihoodTable(Query.Query)
    RoleFrequency.RoleFrequency.wipeFrequencyVariables(RoleFrequency.RoleFrequency)

    #load Frequencylevels for Openstaan
    RoleFrequency.RoleFrequency.loadOpenstaanFrequencyTable(RoleFrequency.RoleFrequency)
    openstaan = Query.Query.generateOpenstaanLikeihoodTable(Query.Query)
    RoleFrequency.RoleFrequency.wipeFrequencyVariables(RoleFrequency.RoleFrequency)

    #load Frequencylevels for Aanpassen
    RoleFrequency.RoleFrequency.loadAanpassenFrequencyTable(RoleFrequency.RoleFrequency)
    aanpassen = Query.Query.generateAanpassenLikeihoodTable(Query.Query)
    RoleFrequency.RoleFrequency.wipeFrequencyVariables(RoleFrequency.RoleFrequency)

    # load Frequencylevels for Instabiliteit
    RoleFrequency.RoleFrequency.loadInstabiliteitFrequencyTable(RoleFrequency.RoleFrequency)
    instabiliteit = Query.Query.generateInstabiliteitLikeihoodTable(Query.Query)
    RoleFrequency.RoleFrequency.wipeFrequencyVariables(RoleFrequency.RoleFrequency)

    # load Frequencylevels for Conscientieusheid
    RoleFrequency.RoleFrequency.loadConscientieusheidFrequencyTable(RoleFrequency.RoleFrequency)
    conscientieusheid = Query.Query.generateConscientieusheidLikeihoodTable(Query.Query)
    RoleFrequency.RoleFrequency.wipeFrequencyVariables(RoleFrequency.RoleFrequency)

    traits = []
    traits.append(extraversie)
    traits.append(openstaan)
    traits.append(aanpassen)
    traits.append(instabiliteit)
    traits.append(conscientieusheid)

    return json.dumps(traits)

def runSingleFrequencies(context):
    extraversie = extraversieVariant.loadExtraversieVariantTable(context['role_select'], context['extraversie_score'])
    aanpassen = aanpassenVariant.loadAanpassenVariantTable(context['role_select'], context['aanpassen_score'])
    openstaan = openstaanVariant.loadOpenstaanVariantTable(context['role_select'], context['openstaan_score'])
    instabiliteit = instabiliteitVariant.loadInstabiliteitVariantTable(context['role_select'], context['instabiliteit_score'])
    conscientieusheid = conscientieusheidVariant.loadConscientieusheidVariantTable(context['role_select'], context['conscientieusheid_score'])

    traits = []
    traits.append(extraversie)
    traits.append(aanpassen)
    traits.append(openstaan)
    traits.append(instabiliteit)
    traits.append(conscientieusheid)

    return traits

def runLoopbaanplanning(context):
    Query.Query.loopbaanRoles = []
    Query.Query.loopbaanLevels = []
    Query.Query.loopbaanYears = []
    Query.Query.loopbaanLevelRoleNames = []

    similarRoleAndLevelResults = Query.Query.getSimilarRoleAndLevelResults(Query.Query, context['role'], context['level'])

    if context['level'] == 1:
        minimum = int(context['achieved_result']) - int(RoleFrequency.RoleFrequency.assistantBaseScore)
        maximum = int(context['achieved_result']) + int(RoleFrequency.RoleFrequency.assistantBaseScore)
    elif context['level'] == 2:
        minimum = int(context['achieved_result']) - int(RoleFrequency.RoleFrequency.generalWorkerBaseScore)
        maximum = int(context['achieved_result']) + int(RoleFrequency.RoleFrequency.generalWorkerBaseScore)
    else:
        minimum = int(context['achieved_result']) - int(RoleFrequency.RoleFrequency.allrounderBaseScore)
        maximum = int(context['achieved_result']) + int(RoleFrequency.RoleFrequency.allrounderBaseScore)

    similarBPIResults = Query.Query.getSimilarBPIResults(Query.Query, similarRoleAndLevelResults, minimum, maximum)

    userResults = Query.Query.getUserResults(Query.Query, similarBPIResults)

    loopbaanplanningResults = Query.Query.getLoopbaanPlanningResults(Query.Query, userResults)

    personalLoopbaan = []

    firstYearUserIdList = []
    LatestYearUserIdList = []

    for planning in loopbaanplanningResults:
        latest_year = Query.Query.getLatestYear(Query.Query, planning)
        for row in planning:
            if row[0] not in firstYearUserIdList:
                firstYearUserIdList.append(row[0])
                firstYearRole = row[3]
                firstYearLevel = row[4]

            if row['year'] == latest_year and row[0] not in LatestYearUserIdList:
                LatestYearUserIdList.append(row[0])
                levelRoleName = ''

                if int(row[3]) == int(firstYearRole) and int(row[4]) == int(firstYearLevel) and int(row['year']) != int(context['year']):
                    addToPersonalLoopbaanplanning(row)
                elif int(row[3]) != int(context['role']) or int(row[4]) != int(context['level']):
                    addToPersonalLoopbaanplanning(row)

    personalLoopbaan.append(Query.Query.loopbaanRoles)
    personalLoopbaan.append(Query.Query.loopbaanLevels)
    personalLoopbaan.append(Query.Query.loopbaanYears)
    personalLoopbaan.append(Query.Query.loopbaanLevelRoleNames)

    return personalLoopbaan

# Add each similar result into the loopbaanplanning
def addToPersonalLoopbaanplanning(row):

    if row['level'] == 1:
        levelRoleName = "Junior"
    elif row['level'] == 2:
        levelRoleName = "Medior"
    else:
        levelRoleName = "Senior"

    if row['role'] == 1:
        levelRoleName += " Assistant"
    elif row['role'] == 2:
        levelRoleName += " GeneralWorker"
    elif row['role'] == 3:
        levelRoleName += " AllRounder"
    elif row['role'] == 4:
        levelRoleName += " Vakspecialist"

    Query.Query.loopbaanRoles.append(row['role'])
    Query.Query.loopbaanLevels.append(row['level'])
    Query.Query.loopbaanYears.append(row['year'])
    Query.Query.loopbaanLevelRoleNames.append(levelRoleName)

# Retrieve the full function name of the user
def getFunction(role, level):
    role = int(role)
    level = int(level)

    if level == 1:
        function = "Junior"
    elif level == 2:
        function = "Medior"
    else:
        function = "Senior"

    if role == 1:
        function += " Assistant"
    elif role == 2:
        function += " GeneralWorker"
    elif role == 3:
        function += " AllRounder"
    elif role == 4:
        function += " Vakspecialist"

    return function