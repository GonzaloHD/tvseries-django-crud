from django.shortcuts import render

from crudseriesapp.models import Series, Character, Suggestions


def home(request):
    series = Series()
    series_list, text = series.find_all()
    context = {
        "list_series": series_list,
        "error": text
    }
    return render(request, "working/homepage.html", context)


def view_series(request):
    series = Series()
    info_series = None
    characters = False
    try:
        id_series = int(request.GET['idseries'])
        characters = request.GET['characters']
        if characters == 'true':
            characters = True
        else:
            characters = False
        info_series, error = series.find_by_id(int(id_series))
    except KeyError as e:
        print("view series key error", e)
        error = e
    except ValueError as err:
        print("view series value error", err)
        error = err
    context = {
        "info_series": info_series,
        "view_characters": characters,
        "error": error
    }
    return render(request, "working/seriesdetail.html", context)


def new_series(request):
    return render(request, "working/newseries.html")


def insert_series(request):
    series = Series()
    try:
        name = request.POST['name']
        image = request.POST['image']
        score = float(request.POST['score'])
        year = int(request.POST['year'])
        result, error = series.save(name, image, score, year)
    except KeyError as e:
        print(e)
        error = e
    except ValueError as err:
        print(err)
        error = err

    series_list, findall_text = series.find_all()
    contexto = {
        "list_series": series_list,
        "error": error,
    }
    return render(request, "working/homepage.html", contexto)


def modify_series(request):
    try:
        id_series = request.GET['idseries']
        name = request.GET['name']
        image = request.GET['image']
        score = request.GET['score']
        year = request.GET['year']
        context = {
            'idseries': id_series,
            'name': name,
            'image': image,
            'score': score,
            'year': year,
        }
    except KeyError as e:
        print(e)
        context = {}
    except ValueError as err:
        print(err)
        context = {}

    return render(request, "working/modifyseries.html", context)


def change_series(request):
    series = Series()
    id_series = None
    try:
        id_series = int(request.POST['idseries'])
        name = request.POST['name']
        image = request.POST['image']
        score = float(request.POST['score'])
        year = int(request.POST['year'])
        result, error = series.modify(id_series, name, image, score, year)
    except KeyError as e:
        print(e)
        error = e
    except ValueError as err:
        print(err)
        error = err
    series_list, findall_text = series.find_all()
    context = {
        'list_series': series_list,
        'id_act_series': id_series,
        'error': error,
    }
    return render(request, "working/homepage.html", context)


def delete_series(request):
    series = Series()
    try:
        id_series = int(request.GET['id_series'])
        result, error = series.delete(id_series)
    except KeyError as e:
        error = e
    except ValueError as err:
        error = err
    series_list, findall_error = series.find_all()
    print(error)
    context = {
        'error': error,
        'list_series': series_list,
    }
    return render(request, "working/homepage.html", context)


def view_characters(request):
    character = Character()
    character_list = None
    try:
        id_series = request.GET['idseries']
        character_list, error = character.find_by_id_series(int(id_series))
    except KeyError as e:
        print(e)
        error = e
    except ValueError as err:
        print(err)
        error = err
    contexto = {
        "list_characters": character_list,
        "error": error
    }
    return render(request, "working/viewcharacters.html", contexto)


def newCharacter(request):
    try:
        id_series = request.GET['idseries']
    except KeyError as e:
        error = e
        id_series = 0
    context = {
        'idseries': id_series,

    }
    return render(request, "working/newcharacter.html", context)


def insertCharacter(request):
    series = Series()
    character = Character()
    character_list = False
    id_series = None
    try:
        id_series = int(request.POST['idseries'])
        name = request.POST['name']
        image = request.POST['image']
        result, error = character.save(name, image, id_series)
        character_list = True
    except KeyError as e:
        print("key error", e)
        error = e
    except ValueError as err:
        print("value error", err)
        error = err

    series_list, series_error = series.find_all()

    contexto = {
        'list_series': series_list,
        'list_characters': character_list,
        'id_act_series': id_series,
        'error': error,
    }
    return render(request, "working/homepage.html", contexto)


def modify_character(request):
    try:
        id_series = int(request.GET['idseries'])
        id_character = int(request.GET['idcharacter'])
        name = request.GET['name']
        image = request.GET['image']
        context = {
            'idseries': id_series,
            'idcharacter': id_character,
            'name': name,
            'image': image,
            'error': ''
        }
    except KeyError as e:
        context = {
            'error': e
        }
    except ValueError as err:
        context = {
            'error': err,
        }
    return render(request, "working/modifycharacter.html", context)


def change_character(request):
    character = Character()
    series = Series()
    character_list = False
    id_series = None
    try:
        id_character = int(request.POST['idcharacter'])
        id_series = int(request.POST['idseries'])
        name = request.POST['name']
        image = request.POST['image']
        result, error = character.modify(id_character, name, image, id_series)
        character_list = True
    except KeyError as e:
        print("key error", e)
        error = e
    except ValueError as err:
        print("value error", err)
        error = err

    series_list, series_error = series.find_all()
    context = {
        'list_series': series_list,
        'list_characters': character_list,
        'id_act_series': id_series,
        'error': error,
    }
    return render(request, "working/homepage.html", context)


def delete_character(request):
    character = Character()
    series = Series()
    character_list = False
    id_series = None
    try:
        id_character = int(request.GET['idcharacter'])
        id_series = int(request.GET['idseries'])
        result, error = character.delete(id_character)
        character_list = True
    except KeyError as e:
        print("key error: ", e)
        error = e
    except ValueError as err:
        print(err)
        error = err
    series_list, error_series = series.find_all()
    context = {
        'list_series': series_list,
        'list_characters': character_list,
        'id_act_series': id_series,
        'error': error,
    }
    return render(request, "working/homepage.html", context)


def suggest_series(request):
    suggest = Suggestions()
    series = suggest.get_series()
    context = {
        'suggested_series': series[0],
    }
    print(series[0])
    print(type(series[0]))
    return render(request, "working/suggestseries.html", context)
