from google.oauth2 import service_account

SCOPES = ["https://www.googleapis.com/auth/calendar"]

def get_creds():
    credentials = service_account.Credentials.from_service_account_file("auth/key.json")
    scoped_credentials = credentials.with_scopes(SCOPES)
    return credentials, scoped_credentials


def get_birthdays(path_to_birthdays):
    birthdays = []
    with open(path_to_birthdays, "r") as f:
        for line in f.readlines():
            birthdays.append(line.split(","))
    return birthdays
