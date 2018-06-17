import python.Role.Assistant as Assistant
import python.Role.GeneralWorker as GeneralWorker
import python.Role.AllRounder as AllRounder
import python.Role.Vakspecialist as Vakspecialist
import python.Role.RoleFrequency as RoleFrequency

def loadAanpassenVariantTable(role, aanpassen_score):
    aanpassenPassed = []
    aanpassenFailed = []

    aanpassenPassedResult = []
    aanpassenFailedResult = []

    role = int(role)

    if role == 1:
        variant_level = RoleFrequency.RoleFrequency.assistantBaseScore
        variant_level_bottom = int(aanpassen_score) - int(variant_level)
        variant_level_top = int(aanpassen_score) + int(variant_level)

        aanpassenPassedResult = Assistant.Assistant.getAanpassenPassedResult(Assistant.Assistant)
        aanpassenFailedResult = Assistant.Assistant.getAanpassenFailedResult(Assistant.Assistant)
    elif role == 2:
        variant_level = RoleFrequency.RoleFrequency.generalWorkerBaseScore
        variant_level_bottom = int(aanpassen_score) - int(variant_level)
        variant_level_top = int(aanpassen_score) + int(variant_level)

        aanpassenPassedResult = GeneralWorker.GeneralWorker.getAanpassenPassedResult(GeneralWorker.GeneralWorker)
        aanpassenFailedResult = GeneralWorker.GeneralWorker.getAanpassenFailedResult(GeneralWorker.GeneralWorker)
    elif role == 3:
        variant_level = RoleFrequency.RoleFrequency.allrounderBaseScore
        variant_level_bottom = int(aanpassen_score) - int(variant_level)
        variant_level_top = int(aanpassen_score) + int(variant_level)

        aanpassenPassedResult = AllRounder.AllRounder.getAanpassenPassedResult(AllRounder.AllRounder)
        aanpassenFailedResult = AllRounder.AllRounder.getAanpassenFailedResult(AllRounder.AllRounder)
    elif role == 4:
        variant_level = RoleFrequency.RoleFrequency.vakspecialistBaseScore
        variant_level_bottom = int(aanpassen_score) - int(variant_level)
        variant_level_top = int(aanpassen_score) + int(variant_level)

        aanpassenPassedResult = Vakspecialist.Vakspecialist.getAanpassenPassedResult(Vakspecialist.Vakspecialist)
        aanpassenFailedResult = Vakspecialist.Vakspecialist.getAanpassenFailedResult(Vakspecialist.Vakspecialist)

    for passed in aanpassenPassedResult:
        if int(passed) >= variant_level_bottom and int(passed) <= variant_level_top:
            aanpassenPassed.append(passed)

    for failed in aanpassenFailedResult:
        if int(failed) >= variant_level_bottom and int(failed) <= variant_level_top:
            aanpassenFailed.append(failed)

    # Retrieve the overall results
    if aanpassenPassed:
        # Retrieve the overall results
        PassedCalculation = round(len(aanpassenPassed) / (len(aanpassenPassed) + len(aanpassenFailed)), 2)
    else:
        PassedCalculation = 0

    if aanpassenFailed:
        FailedCalculation = round(len(aanpassenFailed) / (len(aanpassenPassed) + len(aanpassenFailed)), 2)
    else:
        FailedCalculation = 0

    # Generate a top level dataset
    aanpassenResults = {}
    aanpassenResults['aanpassenPassedSum'] = len(aanpassenPassed)
    aanpassenResults['aanpassenFailedSum'] = len(aanpassenFailed)
    aanpassenResults['aanpassenSum'] = len(aanpassenPassed) + len(aanpassenFailed)
    aanpassenResults['aanpassenPassedCalculation'] = PassedCalculation
    aanpassenResults['aanpassenFailedCalculation'] = FailedCalculation

    return aanpassenResults
