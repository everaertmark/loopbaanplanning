import python.Role.Assistant as Assistant
import python.Role.GeneralWorker as GeneralWorker
import python.Role.AllRounder as AllRounder
import python.Role.Vakspecialist as Vakspecialist
import python.Role.RoleFrequency as RoleFrequency

def loadOpenstaanVariantTable(role, openstaan_score):
    openstaanPassed = []
    openstaanFailed = []

    openstaanPassedResult = []
    openstaanFailedResult = []

    role = int(role)

    if role == 1:
        variant_level = RoleFrequency.RoleFrequency.assistantBaseScore
        variant_level_bottom = int(openstaan_score) - int(variant_level)
        variant_level_top = int(openstaan_score) + int(variant_level)

        openstaanPassedResult = Assistant.Assistant.getOpenstaanPassedResult(Assistant.Assistant)
        openstaanFailedResult = Assistant.Assistant.getOpenstaanFailedResult(Assistant.Assistant)
    elif role == 2:
        variant_level = RoleFrequency.RoleFrequency.generalWorkerBaseScore
        variant_level_bottom = int(openstaan_score) - int(variant_level)
        variant_level_top = int(openstaan_score) + int(variant_level)

        openstaanPassedResult = GeneralWorker.GeneralWorker.getOpenstaanPassedResult(GeneralWorker.GeneralWorker)
        openstaanFailedResult = GeneralWorker.GeneralWorker.getOpenstaanFailedResult(GeneralWorker.GeneralWorker)
    elif role == 3:
        variant_level = RoleFrequency.RoleFrequency.allrounderBaseScore
        variant_level_bottom = int(openstaan_score) - int(variant_level)
        variant_level_top = int(openstaan_score) + int(variant_level)

        openstaanPassedResult = AllRounder.AllRounder.getOpenstaanPassedResult(AllRounder.AllRounder)
        openstaanFailedResult = AllRounder.AllRounder.getOpenstaanFailedResult(AllRounder.AllRounder)
    elif role == 4:
        variant_level = RoleFrequency.RoleFrequency.vakspecialistBaseScore
        variant_level_bottom = int(openstaan_score) - int(variant_level)
        variant_level_top = int(openstaan_score) + int(variant_level)

        openstaanPassedResult = Vakspecialist.Vakspecialist.getOpenstaanPassedResult(Vakspecialist.Vakspecialist)
        openstaanFailedResult = Vakspecialist.Vakspecialist.getOpenstaanFailedResult(Vakspecialist.Vakspecialist)

    for passed in openstaanPassedResult:
        if int(passed) >= variant_level_bottom and int(passed) <= variant_level_top:
            openstaanPassed.append(passed)

    for failed in openstaanFailedResult:
        if int(failed) >= variant_level_bottom and int(failed) <= variant_level_top:
            openstaanFailed.append(failed)

    # Retrieve the overall results
    if openstaanPassed:
        # Retrieve the overall results
        PassedCalculation = round(len(openstaanPassed) / (len(openstaanPassed) + len(openstaanFailed)), 2)
    else:
        PassedCalculation = 0

    if openstaanFailed:
        FailedCalculation = round(len(openstaanFailed) / (len(openstaanPassed) + len(openstaanFailed)), 2)
    else:
        FailedCalculation = 0

    # Generate a top level dataset
    openstaanResults = {}
    openstaanResults['openstaanPassedSum'] = len(openstaanPassed)
    openstaanResults['openstaanFailedSum'] = len(openstaanFailed)
    openstaanResults['openstaanSum'] = len(openstaanPassed) + len(openstaanFailed)
    openstaanResults['openstaanPassedCalculation'] = PassedCalculation
    openstaanResults['openstaanFailedCalculation'] = FailedCalculation

    return openstaanResults
