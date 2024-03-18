from datetime import date, timedelta

CURR_YEAR = date.today().year


def create_birthday_event(person_name, month, day, reminder="popup"):
    # Used to get end date of event, handle end of month
    end_date = date(year=CURR_YEAR, month=month, day=day) + timedelta(days=1)
    return {
        "calendarId": "primary",
        "description": f"Birthday of {person_name}",
        "end": {
            "date": f"{end_date.year}-{end_date.month}-{end_date.day}",
            "timeZone": "Europe/Paris"
        },
        "start": {
            "date": f"{CURR_YEAR}-{month}-{day}",
            "timeZone": "Europe/Paris"
        },
        "recurrence": [
            "RRULE:FREQ=YEARLY;COUNT=1"
        ]
    }


def get_birthdays(path_to_birthdays):
    birthdays = []
    with open(path_to_birthdays, "r") as f:
        for line in f.readlines():
            birthdays.append(line.split(","))
    return birthdays
