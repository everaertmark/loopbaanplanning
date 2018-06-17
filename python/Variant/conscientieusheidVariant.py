import python.Role.Assistant as Assistant
import python.Role.GeneralWorker as GeneralWorker
import python.Role.AllRounder as AllRounder
import python.Role.Vakspecialist as Vakspecialist
import python.Role.RoleFrequency as RoleFrequency

def loadConscientieusheidVariantTable(role, conscientieusheid_score):
    conscientieusheidPassed = []
    conscientieusheidFailed = []

    conscientieusheidPassedResult = []
    conscientieusheidFailedResult = []

    role = int(role)

    if role == 1:
        variant_level = RoleFrequency.RoleFrequency.assistantBaseScore
        variant_level_bottom = int(conscientieusheid_score) - int(variant_level)
        variant_level_top = int(conscientieusheid_score) + int(variant_level)

        conscientieusheidPassedResult = Assistant.Assistant.getConscientieusheidPassedResult(Assistant.Assistant)
        conscientieusheidFailedResult = Assistant.Assistant.getConscientieusheidFailedResult(Assistant.Assistant)
    elif role == 2:
        variant_level = RoleFrequency.RoleFrequency.generalWorkerBaseScore
        variant_level_bottom = int(conscientieusheid_score) - int(variant_level)
        variant_level_top = int(conscientieusheid_score) + int(variant_level)

        conscientieusheidPassedResult = GeneralWorker.GeneralWorker.getConscientieusheidPassedResult(GeneralWorker.GeneralWorker)
        conscientieusheidFailedResult = GeneralWorker.GeneralWorker.getConscientieusheidFailedResult(GeneralWorker.GeneralWorker)
    elif role == 3:
        variant_level = RoleFrequency.RoleFrequency.allrounderBaseScore
        variant_level_bottom = int(conscientieusheid_score) - int(variant_level)
        variant_level_top = int(conscientieusheid_score) + int(variant_level)

        conscientieusheidPassedResult = AllRounder.AllRounder.getConscientieusheidPassedResult(AllRounder.AllRounder)
        conscientieusheidFailedResult = AllRounder.AllRounder.getConscientieusheidFailedResult(AllRounder.AllRounder)
    elif role == 4:
        variant_level = RoleFrequency.RoleFrequency.vakspecialistBaseScore
        variant_level_bottom = int(conscientieusheid_score) - int(variant_level)
        variant_level_top = int(conscientieusheid_score) + int(variant_level)

        conscientieusheidPassedResult = Vakspecialist.Vakspecialist.getConscientieusheidPassedResult(Vakspecialist.Vakspecialist)
        conscientieusheidFailedResult = Vakspecialist.Vakspecialist.getConscientieusheidFailedResult(Vakspecialist.Vakspecialist)

    for passed in conscientieusheidPassedResult:
        if int(passed) >= variant_level_bottom and int(passed) <= variant_level_top:
            conscientieusheidPassed.append(passed)

    for failed in conscientieusheidFailedResult:
        if int(failed) >= variant_level_bottom and int(failed) <= variant_level_top:
            conscientieusheidFailed.append(failed)

    # Retrieve the overall results  
    if conscientieusheidPassed:
        # Retrieve the overall results
        PassedCalculation = round(len(conscientieusheidPassed) / (len(conscientieusheidPassed) + len(conscientieusheidFailed)), 2)
    else:
        PassedCalculation = 0

    if conscientieusheidFailed:
        FailedCalculation = round(len(conscientieusheidFailed) / (len(conscientieusheidPassed) + len(conscientieusheidFailed)), 2)
    else:
        FailedCalculation = 0

    # Generate a top level dataset
    conscientieusheidResults = {}
    conscientieusheidResults['conscientieusheidPassedSum'] = len(conscientieusheidPassed)
    conscientieusheidResults['conscientieusheidFailedSum'] = len(conscientieusheidFailed)
    conscientieusheidResults['conscientieusheidSum'] = len(conscientieusheidPassed) + len(conscientieusheidFailed)
    conscientieusheidResults['conscientieusheidPassedCalculation'] = PassedCalculation
    conscientieusheidResults['conscientieusheidFailedCalculation'] = FailedCalculation

    return conscientieusheidResults