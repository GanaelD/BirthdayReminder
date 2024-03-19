import datetime
import utils
from tqdm import tqdm

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.events"]

SECRET_PATH = "../auth/secret.json"
TOKEN_PATH = "../auth/token.json"
BIRTHDAYS_PATH = "../birthdays.txt"
birthdays = utils.get_birthdays(BIRTHDAYS_PATH)


def main():
    creds = utils.get_creds()

    try:
        service = build("calendar", "v3", credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
        print("Sending every birthday\n")

        for birthday in tqdm(birthdays):
            print(f"Creating event for birthday of {birthday[0]}")
            birthday_event = utils.create_birthday_event(*birthday)

            event_result = (
                service
                .events()
                .insert(calendarId="primary", body=birthday_event)
                .execute()
            )

    except HttpError as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()
