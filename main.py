import utils

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SECRET_FILE = "auth/key.json"

def main():
    creds, scoped_creds = utils.get_creds()
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                SECRET_FILE, utils.SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(SECRET_FILE, "w") as token:
            token.write(creds.to_json())
    try:
        service = build("calendar", "v3", credentials=creds)

        # Call the Calendar API
