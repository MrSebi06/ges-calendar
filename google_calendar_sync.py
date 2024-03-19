from datetime import timezone
import os
from ics import Calendar
from googleapiclient.discovery import build

import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

CREDENTIALS_FILE = 'credentials.json'

def get_calendar_service():
   creds = None
   if os.path.exists('token.pickle'):
       with open('token.pickle', 'rb') as token:
           creds = pickle.load(token)
   if not creds or not creds.valid:
       if creds and creds.expired and creds.refresh_token:
           creds.refresh(Request())
       else:
           flow = InstalledAppFlow.from_client_secrets_file(
               CREDENTIALS_FILE, SCOPES)
           creds = flow.run_local_server(port=0)

       with open('token.pickle', 'wb') as token:
           pickle.dump(creds, token)

   service = build('calendar', 'v3', credentials=creds)
   return service

def main():
    service = get_calendar_service()
    
    with open('calendar.ics', 'rb') as ics:
        c = Calendar(ics.read().decode('iso-8859-1'))
        for event in c.events:
            gevent = {
                'summary': event.name,
                'location': event.location,
                'organizer': {
                    'displayName': event.description,
                },
                'start': {
                    'dateTime': event.begin.astimezone(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S'),
                    'timeZone': 'GMT+00:00',
                },
                'end': {
                    'dateTime': event.end.astimezone(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S'),
                    'timeZone': 'GMT+00:00',
                },
                'attendees': [
                    {
                    'email': f'{os.getenv("LOGIN")}@myges.fr',
                    'displayName': os.getenv("LOGIN"),
                    },
                ],
                'iCalUID': event.uid,
            }

            imported_event = service.events().import_(calendarId=os.getenv("CALENDAR_ID"), body=gevent).execute()

            print(imported_event['id'])
            
    service.close()


if __name__ == '__main__':
    main()