import python.Personal as Personal
import json as json

likeihoodtable = []

def generateLikeihoodTable():

    # Retrieve the overall results
    overallPassedSum = Personal.Personal.aanpassenPassed + Personal.Personal.extraversiePassed + Personal.Personal.conscientieusheidPassed + Personal.Personal.instabiliteitPassed + Personal.Personal.openstaanPassed
    overallFailedSum = Personal.Personal.aanpassenFailed + Personal.Personal.extraversieFailed + Personal.Personal.conscientieusheidFailed + Personal.Personal.instabiliteitFailed + Personal.Personal.openstaanFailed
    overallSum = Personal.Personal.aanpassenSum + Personal.Personal.extraversieSum + Personal.Personal.conscientieusheidSum + Personal.Personal.instabiliteitSum + Personal.Personal.openstaanSum
    PassedCalculation = round(overallPassedSum / overallSum, 2)
    FailedCalculation = round(overallFailedSum / overallSum, 2)

    # Generate a top level dataset
    overallResults = {}
    overallResults['overallPassedSum'] = overallPassedSum
    overallResults['overallFailedSum'] = overallFailedSum
    overallResults['overallSum'] = overallSum
    overallResults['passedCalculation'] = PassedCalculation
    overallResults['failedCalculation'] = FailedCalculation
    # append it to likeihoodtable
    likeihoodtable.append(overallResults)

    # Generate the sub level datasets
    subResults = []

    ExtraversiePassedCalc = round(Personal.Personal.extraversiePassed / overallPassedSum, 2)
    ExtraversieAmountCalc = round(Personal.Personal.extraversieSum / overallPassedSum, 2)
    ExtraversieFinalProb = round((ExtraversiePassedCalc * PassedCalculation) / ExtraversieAmountCalc, 2)

    ExtraversieResults = {}
    ExtraversieResults['ExtraversiePassedCalc'] = ExtraversiePassedCalc
    ExtraversieResults['ExtraversiePassed'] = Personal.Personal.extraversiePassed
    ExtraversieResults['ExtraversieFailed'] = Personal.Personal.extraversieFailed
    ExtraversieResults['ExtraversieProb'] = round((100 / Personal.Personal.extraversieSum) * Personal.Personal.extraversiePassed, 2)
    ExtraversieResults['ExtraversieTotal'] = Personal.Personal.extraversieFailed + Personal.Personal.extraversiePassed
    ExtraversieResults['ExtraversieAmountCalc'] = ExtraversieAmountCalc
    ExtraversieResults['ExtraversieFinalProb'] = ExtraversieFinalProb
    subResults.append(ExtraversieResults)

    AanpassenPassedCalc = round(Personal.Personal.aanpassenPassed / overallPassedSum, 2)
    AanpassenAmountCalc = round(Personal.Personal.aanpassenSum / overallPassedSum, 2)
    AanpassenFinalProb = round((AanpassenPassedCalc * PassedCalculation) / AanpassenAmountCalc, 2)

    AanpassenResults = {}
    AanpassenResults['AanpassenPassedCalc'] = AanpassenPassedCalc
    AanpassenResults['AanpassenPassed'] = Personal.Personal.aanpassenPassed
    AanpassenResults['AanpassenFailed'] = Personal.Personal.aanpassenFailed
    AanpassenResults['AanpassenProb'] = round((100 / Personal.Personal.aanpassenSum) * Personal.Personal.aanpassenPassed, 2)
    AanpassenResults['AanpassenTotal'] = Personal.Personal.aanpassenFailed + Personal.Personal.aanpassenPassed
    AanpassenResults['AanpassenAmountCalc'] = AanpassenAmountCalc
    AanpassenResults['AanpassenFinalCalc'] = AanpassenFinalProb
    subResults.append(AanpassenResults)

    OpenstaanPassedCalc = round(Personal.Personal.openstaanPassed / overallPassedSum, 2)
    OpenstaanAmountCalc = round(Personal.Personal.openstaanSum / overallPassedSum, 2)
    OpenstaanFinalProb = round((OpenstaanPassedCalc * PassedCalculation) / OpenstaanAmountCalc, 2)

    OpenstaanResults = {}
    OpenstaanResults['OpenstaanPassedCalc'] = OpenstaanPassedCalc
    OpenstaanResults['OpenstaanPassed'] = Personal.Personal.aanpassenPassed
    OpenstaanResults['OpenstaanFailed'] = Personal.Personal.aanpassenFailed
    OpenstaanResults['OpenstaanProb'] = round((100 / Personal.Personal.openstaanSum) * Personal.Personal.openstaanPassed, 2)
    OpenstaanResults['OpenstaanTotal'] = Personal.Personal.aanpassenFailed + Personal.Personal.aanpassenPassed
    OpenstaanResults['OpenstaanAmountCalc'] = OpenstaanAmountCalc
    OpenstaanResults['OpenstaanFinalProb'] = OpenstaanFinalProb
    subResults.append(OpenstaanResults)

    InstabiliteitPassedCalc = round(Personal.Personal.instabiliteitPassed / overallPassedSum, 2)
    InstabiliteitAmountCalc = round(Personal.Personal.instabiliteitSum / overallPassedSum, 2)
    InstabiliteitFinalProb = round((InstabiliteitPassedCalc * PassedCalculation) / InstabiliteitAmountCalc, 2)

    InstabiliteitResults = {}
    InstabiliteitResults['InstabiliteitPassedCalc'] = InstabiliteitPassedCalc
    InstabiliteitResults['InstabiliteitPassed'] = Personal.Personal.instabiliteitPassed
    InstabiliteitResults['InstabiliteitFailed'] = Personal.Personal.instabiliteitFailed
    InstabiliteitResults['InstabiliteitProb'] = round((100 / Personal.Personal.instabiliteitSum) * Personal.Personal.instabiliteitPassed, 2)
    InstabiliteitResults['InstabiliteitTotal'] = Personal.Personal.instabiliteitFailed + Personal.Personal.instabiliteitPassed
    InstabiliteitResults['InstabiliteitAmountCalc'] = InstabiliteitAmountCalc
    InstabiliteitResults['InstabiliteitFinalProb'] = InstabiliteitFinalProb
    subResults.append(InstabiliteitResults)

    ConscientieusheidPassedCalc = round(Personal.Personal.conscientieusheidPassed / overallPassedSum, 2)
    ConscientieusheidAmountCalc = round(Personal.Personal.conscientieusheidSum / overallPassedSum, 2)
    ConscientieusheidFinalProb = round((ConscientieusheidPassedCalc * PassedCalculation) / ConscientieusheidAmountCalc, 2)

    ConscientieusheidResults = {}
    ConscientieusheidResults['ConscientieusheidPassedCalc'] = ConscientieusheidPassedCalc
    ConscientieusheidResults['ConscientieusheidPassed'] = Personal.Personal.conscientieusheidPassed
    ConscientieusheidResults['ConscientieusheidFailed'] = Personal.Personal.conscientieusheidFailed
    ConscientieusheidResults['ConscientieusheidProb'] = round((100 / Personal.Personal.conscientieusheidSum) * Personal.Personal.conscientieusheidPassed, 2)
    ConscientieusheidResults['ConscientieusheidTotal'] = Personal.Personal.conscientieusheidFailed + Personal.Personal.conscientieusheidPassed
    ConscientieusheidResults['ConscientieusheidAmountCalc'] = ConscientieusheidAmountCalc
    ConscientieusheidResults['ConscientieusheidFinalProb'] = ConscientieusheidFinalProb
    subResults.append(ConscientieusheidResults)

    likeihoodtable.append(subResults)

    data = json.dumps(likeihoodtable)

    return data

    # print('PassedProb: ', PassedCalculation)
    # print("")
    # print('ExtraversieYesCalc: ', ExtraversiePassedCalc)
    # print('ExtraversieAmountCalc: ', ExtraversieAmountCalc)
    # print('ExtraversieFinalProb: ', ExtraversieFinalProb)
    # print("")
    # print('AanpassenYesCalc: ', AanpassenPassedCalc)
    # print('AanpassenAmountCalc: ', AanpassenAmountCalc)
    # print('AanpassenFinalProb: ', AanpassenFinalProb)
    # print("")
    # print('OpenstaanYesCalc: ', OpenstaanPassedCalc)
    # print('OpenstaanAmountCalc: ', OpenstaanAmountCalc)
    # print('OpenstaanFinalProb: ', OpenstaanFinalProb)
    # print("")
    # print('InstabiliteitYesCalc: ', InstabiliteitPassedCalc)
    # print('InstabiliteitAmountCalc: ', InstabiliteitAmountCalc)
    # print('InstabiliteitFinalProb: ', InstabiliteitFinalProb)
    # print("")
    # print('ConscientieusheidYesCalc: ', ConscientieusheidPassedCalc)
    # print('ConscientieusheidAmountCalc: ', ConscientieusheidAmountCalc)
    # print('ConscientieusheidFinalProb: ', ConscientieusheidFinalProb)
