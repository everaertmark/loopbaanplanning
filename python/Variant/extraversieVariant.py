import python.Role.Assistant as Assistant
import python.Role.GeneralWorker as GeneralWorker
import python.Role.AllRounder as AllRounder
import python.Role.Vakspecialist as Vakspecialist
import python.Role.RoleFrequency as RoleFrequency

def loadExtraversieVariantTable(role, extraversie_score):
    extraversiePassed = []
    extraversieFailed = []

    extraversiePassedResult = []
    extraversieFailedResult = []

    role = int(role)

    if role == 1:
        variant_level = RoleFrequency.RoleFrequency.assistantBaseScore
        variant_level_bottom = int(extraversie_score) - int(variant_level)
        variant_level_top = int(extraversie_score) + int(variant_level)

        extraversiePassedResult = Assistant.Assistant.getExtraversiePassedResult(Assistant.Assistant)
        extraversieFailedResult = Assistant.Assistant.getExtraversieFailedResult(Assistant.Assistant)
    elif role == 2:
        variant_level = RoleFrequency.RoleFrequency.generalWorkerBaseScore
        variant_level_bottom = int(extraversie_score) - int(variant_level)
        variant_level_top = int(extraversie_score) + int(variant_level)

        extraversiePassedResult = GeneralWorker.GeneralWorker.getExtraversiePassedResult(GeneralWorker.GeneralWorker)
        extraversieFailedResult = GeneralWorker.GeneralWorker.getExtraversieFailedResult(GeneralWorker.GeneralWorker)
    elif role == 3:
        variant_level = RoleFrequency.RoleFrequency.allrounderBaseScore
        variant_level_bottom = int(extraversie_score) - int(variant_level)
        variant_level_top = int(extraversie_score) + int(variant_level)

        extraversiePassedResult = AllRounder.AllRounder.getExtraversiePassedResult(AllRounder.AllRounder)
        extraversieFailedResult = AllRounder.AllRounder.getExtraversieFailedResult(AllRounder.AllRounder)
    elif role == 4:
        variant_level = RoleFrequency.RoleFrequency.vakspecialistBaseScore
        variant_level_bottom = int(extraversie_score) - int(variant_level)
        variant_level_top = int(extraversie_score) + int(variant_level)

        extraversiePassedResult = Vakspecialist.Vakspecialist.getExtraversiePassedResult(Vakspecialist.Vakspecialist)
        extraversieFailedResult = Vakspecialist.Vakspecialist.getExtraversieFailedResult(Vakspecialist.Vakspecialist)

    for passed in extraversiePassedResult:
        if int(passed) >= variant_level_bottom and int(passed) <= variant_level_top:
            extraversiePassed.append(passed)

    for failed in extraversieFailedResult:
        if int(failed) >= variant_level_bottom and int(failed) <= variant_level_top:
            extraversieFailed.append(failed)

    # Retrieve the overall results
    if extraversiePassed:
        # Retrieve the overall results
        PassedCalculation = round(len(extraversiePassed) / (len(extraversiePassed) + len(extraversieFailed)), 2)
    else:
        PassedCalculation = 0

    if extraversieFailed:
        FailedCalculation = round(len(extraversieFailed) / (len(extraversiePassed) + len(extraversieFailed)), 2)
    else:
        FailedCalculation = 0

    # Generate a top level dataset
    extraversieResults = {}
    extraversieResults['extravertPassedSum'] = len(extraversiePassed)
    extraversieResults['extravertFailedSum'] = len(extraversieFailed)
    extraversieResults['extravertSum'] = len(extraversiePassed) + len(extraversieFailed)
    extraversieResults['extravertPassedCalculation'] = PassedCalculation
    extraversieResults['extravertFailedCalculation'] = FailedCalculation

    return extraversieResults
