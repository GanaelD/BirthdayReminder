def create_birthday_event(person_name, month, day, reminder="popup"):
    return {
        "calendarId": "primary",
        "description": "Birthday of {person_name}",
        "end": {
            "date": ""
        },
        "start": {
            "date": ""
        },
        "recurrence": [
            "RRULE"
        ]
    }


def get_birthdays(path_to_birthdays):
    birthdays = []
    with open(path_to_birthdays, "r") as f:
        for line in f.readlines():
            birthdays.append(line.split(","))
    return birthdays
