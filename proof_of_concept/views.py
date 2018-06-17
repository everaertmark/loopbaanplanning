import os
import pandas as pandas

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# importing loading from django template
from django.template import loader
from python import main

# our view which is a function named index
def index(request):
    # getting our template
    template = loader.get_template('index.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render())

def test(request):
    # getting our template
    template = loader.get_template('test.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render())

def showdata(request):
    # getting our template
    template = loader.get_template('showdata.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render())

def runscript(request):
    response = main.runMain()
    return HttpResponse(response)

def runtraitfrequencies(request):
    response = main.runTraitFrequencies()
    return HttpResponse(response)

# disabling csrf (cross site request forgery)
@csrf_exempt
def getformdata(request):
    # if post request came
    if request.method == 'POST':
        # getting values from post
        user_id = request.POST.get('user_id')
        bpi_score = request.POST.get('bpi_score')
        role_select = request.POST.get('role_select')
        level_select = request.POST.get('level_select')
        year_select = request.POST.get('year_select')
        extraversie_score = request.POST.get('extraversie_score')
        aanpassen_score = request.POST.get('aanpassen_score')
        openstaan_score = request.POST.get('openstaan_score')
        instabiliteit_score = request.POST.get('instabiliteit_score')
        conscientieusheid_score = request.POST.get('conscientieusheid_score')

        # adding the values in a context variable
        traitContext = {
            'bpi_score': bpi_score,
            'role_select': role_select,
            'extraversie_score': extraversie_score,
            'aanpassen_score': aanpassen_score,
            'openstaan_score': openstaan_score,
            'instabiliteit_score': instabiliteit_score,
            'conscientieusheid_score': conscientieusheid_score
        }

        loopbaanContext = {
            'user_id': user_id,
            'function': '',
            'role': role_select,
            'level': level_select,
            'achieved_result': bpi_score,
            'year': year_select,
        }

        traitResult = main.runSingleFrequencies(traitContext)

        loopbaanplanning = main.runLoopbaanplanning(loopbaanContext)

        context = {
            'role': role_select,
            'extraversie': traitResult[0],
            'aanpassen': traitResult[1],
            'openstaan': traitResult[2],
            'instabiliteit': traitResult[3],
            'conscientieusheid': traitResult[4],
            'loopbaanRoles': loopbaanplanning[0],
            'loopbaanLevels': loopbaanplanning[1],
            'loopbaanYears': loopbaanplanning[2],
            'loopbaanLevelRoleNames': loopbaanplanning[3],
            'loopbaanCount': len(loopbaanplanning[3]),
            'loopbaanFunction': main.getFunction(role_select, level_select)
        }

        # getting our showdata template
        template = loader.get_template('showdata.html')

        # returing the template
        return HttpResponse(template.render(context, request))
    else:
        # if post request is not true
        # returing the form template
        template = loader.get_template('index.html')
        return HttpResponse(template.render())

# disabling csrf (cross site request forgery)
@csrf_exempt
def example(request):
    currentPath = os.path.dirname(os.path.dirname(__file__))
    CHARACTER_ATTR_NAMES = ["user_id", "function", "role", "level", "achieved_result", "year"]

    # if post request came
    if request.method == 'POST':
        # getting values from post
        character_select = request.POST.get('character_select')
        characterCSV = "python/testresults/jan.csv"

        if character_select == 'Jan de Vries':
            characterCSV = "python/testresults/jan.csv"
        elif character_select == 'Henk Cornelissen':
            characterCSV = "python/testresults/henk.csv"
        else:
            characterCSV = "python/testresults/piet.csv"

        characterPath = os.path.join(currentPath, characterCSV)

        characterResult = pandas.read_csv(characterPath, names=CHARACTER_ATTR_NAMES, delimiter=',')

        for index, row in characterResult.iterrows():
            # adding the values in a context variable
            context = {
                'user_id': row[0],
                'function': row[1],
                'role': row[2],
                'level': row[3],
                'achieved_result': row[4],
                'year': row[5]
            }

            loopbaanplanning = main.runLoopbaanplanning(context)

            context = {
                'loopbaanRoles': loopbaanplanning[0],
                'loopbaanLevels': loopbaanplanning[1],
                'loopbaanYears': loopbaanplanning[2],
                'loopbaanLevelRoleNames': loopbaanplanning[3],
                'loopbaanCount': len(loopbaanplanning[3]),
                'loopbaanFunction': main.getFunction(row[2], row[3]),
                'characterSelect': character_select
            }
            template = loader.get_template('example.html')
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('example.html')
        return HttpResponse(template.render())