import json


def read(name):
    with open(name + '.json', 'r') as file:
        d = json.load(file)
    return d


def count_weeks():
    return len(read('schedule'))


def count_days():
    summa = 0
    d = read('schedule')
    for key_date in d:
        summa += len(d[key_date])
    return summa


def count_event():
    summa = 0
    d = read('schedule')
    for key_date in d:
        for key_day in d[key_date]:
            summa += len(d[key_date][key_day])
    return summa


def count_lections():
    kol = 0
    d = read('schedule')
    for key_date in d:
        for key_day in d[key_date]:
            for event in d[key_date][key_day]:
                if event['name_lesson'].split()[-1] == "lecture":
                    kol += 1
    return kol

def count_Hours():
    kol = 0
    d = read('schedule')
    for key_date in d:
        for key_day in d[key_date]:
            for event in d[key_date][key_day]:
                print(event["time"])



count_Hours()