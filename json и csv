import json
import csv
def creat_csv():
    kol = 0
    with open("schedule (1).json", "r") as file:
        d = json.load(file)
        with open("English.csv", "w") as file:
            writer = csv.writer(file, delimiter=";")
            for key_week in d:
                for key_data in d[key_week]:
                    for event in d[key_week][key_data]:

                        if "English" in event["name_lesson"]:

                            if kol == 0:
                                writer.writerow(["date", "time", "name_lesson", "auditorium", "name_of_the_teacher", "teachers_schedule"])
                                writer.writerow([event["date"], event["time"], event["name_lesson"], event["auditorium"],event["name_of_the_teacher"], event["teachers_schedule"]])
                                kol += 1

                            else:
                                writer.writerow([event["date"], event["time"], event["name_lesson"], event["auditorium"], event["name_of_the_teacher"], event["teachers_schedule"]])

print(creat_csv())