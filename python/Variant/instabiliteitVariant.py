import python.Role.Assistant as Assistant
import python.Role.GeneralWorker as GeneralWorker
import python.Role.AllRounder as AllRounder
import python.Role.Vakspecialist as Vakspecialist
import python.Role.RoleFrequency as RoleFrequency

def loadInstabiliteitVariantTable(role, instabiliteit_score):
    instabiliteitPassed = []
    instabiliteitFailed = []

    instabiliteitPassedResult = []
    instabiliteitFailedResult = []

    role = int(role)

    if role == 1:
        variant_level = RoleFrequency.RoleFrequency.assistantBaseScore
        variant_level_bottom = int(instabiliteit_score) - int(variant_level)
        variant_level_top = int(instabiliteit_score) + int(variant_level)

        instabiliteitPassedResult = Assistant.Assistant.getInstabiliteitPassedResult(Assistant.Assistant)
        instabiliteitFailedResult = Assistant.Assistant.getInstabiliteitFailedResult(Assistant.Assistant)
    elif role == 2:
        variant_level = RoleFrequency.RoleFrequency.generalWorkerBaseScore
        variant_level_bottom = int(instabiliteit_score) - int(variant_level)
        variant_level_top = int(instabiliteit_score) + int(variant_level)

        instabiliteitPassedResult = GeneralWorker.GeneralWorker.getInstabiliteitPassedResult(GeneralWorker.GeneralWorker)
        instabiliteitFailedResult = GeneralWorker.GeneralWorker.getInstabiliteitFailedResult(GeneralWorker.GeneralWorker)
    elif role == 3:
        variant_level = RoleFrequency.RoleFrequency.allrounderBaseScore
        variant_level_bottom = int(instabiliteit_score) - int(variant_level)
        variant_level_top = int(instabiliteit_score) + int(variant_level)

        instabiliteitPassedResult = AllRounder.AllRounder.getInstabiliteitPassedResult(AllRounder.AllRounder)
        instabiliteitFailedResult = AllRounder.AllRounder.getInstabiliteitFailedResult(AllRounder.AllRounder)
    elif role == 4:
        variant_level = RoleFrequency.RoleFrequency.vakspecialistBaseScore
        variant_level_bottom = int(instabiliteit_score) - int(variant_level)
        variant_level_top = int(instabiliteit_score) + int(variant_level)

        instabiliteitPassedResult = Vakspecialist.Vakspecialist.getInstabiliteitPassedResult(Vakspecialist.Vakspecialist)
        instabiliteitFailedResult = Vakspecialist.Vakspecialist.getInstabiliteitFailedResult(Vakspecialist.Vakspecialist)

    for passed in instabiliteitPassedResult:
        if int(passed) >= variant_level_bottom and int(passed) <= variant_level_top:
            instabiliteitPassed.append(passed)

    for failed in instabiliteitFailedResult:
        if int(failed) >= variant_level_bottom and int(failed) <= variant_level_top:
            instabiliteitFailed.append(failed)

    # Retrieve the overall results
    if instabiliteitPassed:
        # Retrieve the overall results
        PassedCalculation = round(len(instabiliteitPassed) / (len(instabiliteitPassed) + len(instabiliteitFailed)), 2)
    else:
        PassedCalculation = 0

    if instabiliteitFailed:
        FailedCalculation = round(len(instabiliteitFailed) / (len(instabiliteitPassed) + len(instabiliteitFailed)), 2)
    else:
        FailedCalculation = 0

    # Generate a top level dataset
    instabiliteitResults = {}
    instabiliteitResults['instabiliteitPassedSum'] = len(instabiliteitPassed)
    instabiliteitResults['instabiliteitFailedSum'] = len(instabiliteitFailed)
    instabiliteitResults['instabiliteitSum'] = len(instabiliteitPassed) + len(instabiliteitFailed)
    instabiliteitResults['instabiliteitPassedCalculation'] = PassedCalculation
    instabiliteitResults['instabiliteitFailedCalculation'] = FailedCalculation

    return instabiliteitResults
