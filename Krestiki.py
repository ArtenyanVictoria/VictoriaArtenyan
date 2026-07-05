import json
with open("schedule.json", "r") as file:
    d = json.load(file)
    for key_weeks in d:
        for key_data in d[key_week]:
            for x in d[key_week][key_data]:
                for key_shedule in d[key_week][key_data][x]:
                    