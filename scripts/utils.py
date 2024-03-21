from datetime import date, timedelta
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

CURR_YEAR = date.today().year
SCOPES = ["https://www.googleapis.com/auth/calendar.events",
          "https://www.googleapis.com/auth/calendar"]
SECRET_PATH = "../auth/secret.json"
TOKEN_PATH = "../auth/token.json"


def get_creds():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
        # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                SECRET_PATH, SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(TOKEN_PATH, "w") as token:
            token.write(creds.to_json())
    return creds


def create_birthday_event(person_name: str, month: int, day: int,
                          reminder_method: str = "popup", reminder_min: int = 0,
                          time_zone: str = "Europe/Paris") -> dict:
    # Don't set a reminder event for the current year if the birthday has already happened
    first_year_event = CURR_YEAR if date.today() < date(CURR_YEAR, month, day) else CURR_YEAR + 1
    # Used to get end date of event, handle end of month
    end_date = date(year=first_year_event, month=month, day=day) + timedelta(days=1)
    return {
        "calendarId": "primary",
        "description": f"Remember to wish {person_name} a happy birthday!",
        "end": {
            "date": f"{end_date.year}-{end_date.month}-{end_date.day}",
            "timeZone": time_zone
        },
        "summary": f"Birthday of {person_name}!",
        "start": {
            "date": f"{first_year_event}-{month}-{day}",
            "timeZone": time_zone
        },
        "recurrence": [
            "RRULE:FREQ=YEARLY"
        ]
    }


def get_birthdays(path_to_birthdays):
    birthdays = []
    with open(path_to_birthdays, "r", encoding="utf8") as f:
        for line in f.readlines():
            birthdays.append(line.split(","))
    for birthday in birthdays:
        try:
            birthday[1], birthday[2] = int(birthday[1]), int(birthday[2])
        except ValueError:
            pass
    return birthdays
