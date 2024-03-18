from datetime import date, timedelta

CURR_YEAR = date.today().year


def create_birthday_event(person_name, month, day, reminder="popup"):
    # Used to get end date of event, handle end of month
    end_date = date(year=CURR_YEAR, month=month, day=day) + timedelta(days=1)
    return {
        "calendarId": "primary",
        "description": f"Remember to wish {person_name} a happy birthday!",
        "end": {
            "date": f"{end_date.year}-{end_date.month}-{end_date.day}",
            "timeZone": "Europe/Paris"
        },
        "summary": f"Birthday of {person_name}!",
        "start": {
            "date": f"{CURR_YEAR}-{month}-{day}",
            "timeZone": "Europe/Paris"
        },
        "recurrence": [
            "RRULE:FREQ=YEARLY"
        ]
    }


def get_birthdays(path_to_birthdays):
    birthdays = []
    with open(path_to_birthdays, "r") as f:
        for line in f.readlines():
            birthdays.append(line.split(","))
    for birthday in birthdays:
        try:
            birthday[1], birthday[2] = int(birthday[1]), int(birthday[2])
        except ValueError:
            pass
    return birthdays
