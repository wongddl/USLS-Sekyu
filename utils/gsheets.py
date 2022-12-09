from googleapiclient.discovery import build
from google.oauth2 import service_account


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'reqs/keys.json'
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
SAMPLE_SPREADSHEET_ID = '1dh-AGmLx17rxFPaVD_OTQqYswTMXN4Ujiv_PSAk0jds'
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()



DISCORD_TOKEN = str(service.spreadsheets().values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                     range='keys_token!B1:B1').execute().get('values'))[3:-3]
SENDGRID_API_KEY = str(service.spreadsheets().values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                    range='keys_token!B2:B2').execute().get('values',[]))[3:-3]
SENDGRID_EMAIL = str(service.spreadsheets().values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                    range='keys_token!B3:B3').execute().get('values',[]))[3:-3]


def append_user(registration_data):
    sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='database!A3', 
                    valueInputOption='USER_ENTERED', body={'values':registration_data}).execute()


def update_email(datanum,message_content):
    service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=f'database!C{datanum}', 
                    valueInputOption='USER_ENTERED', body={'values':[[message_content]]}).execute() 

def update_code(datanum,random_code):
    service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=f'database!D{datanum}', 
                    valueInputOption='USER_ENTERED', body={'values':[[random_code]]}).execute() 

def update_verified(datanum):
    verified = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=f'database!E{datanum}', 
                    valueInputOption='USER_ENTERED', body={'values':[['1']]}).execute() 

def update_anonmsgnum(anonnum):
    append_anonnum = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=f'keys_token!B4', 
                        valueInputOption='USER_ENTERED', body={'values':[[f'{anonnum}']]}).execute()


def get_author():
    get_author = service.spreadsheets().values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                    range='database!A3:A100').execute().get('values',[])
    return get_author

def get_code():
    get_code = service.spreadsheets().values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                    range='database!D3:D100').execute().get('values',[])
    return get_code

def get_email():
    get_email = service.spreadsheets().values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                    range='database!C3:C100').execute().get('values',[])
    return get_email

def get_verify(datanum):
    get_verify = service.spreadsheets().values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                    range=f'database!E{datanum}:E{datanum}').execute().get('values',[])
    return get_verify

def get_verify(datanum):
    get_verify = service.spreadsheets().values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                    range=f'database!E{datanum}:E{datanum}').execute().get('values',[])
    return get_verify

def get_anonmsgnum():
    request_anonnum = service.spreadsheets().values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                        range='keys_token!B4:B4').execute().get('values',[])
    return request_anonnum

