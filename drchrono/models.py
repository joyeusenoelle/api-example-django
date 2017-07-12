from django.db import models, connection
import ast, requests
# Create your models here.

BASE_URL = "https://drchrono.com"

def fetch_drchrono_userdata(dob = None):
    if dob in [None, '']:
        dobstr = ''
    else:
        dobstr = '?date_of_birth=' + dob
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, extra_data from social_auth_usersocialauth")
        row = cursor.fetchone()
    token = ast.literal_eval(row[1])['access_token']
    URI = "".join([BASE_URL,
                  '/api/patients',
                  dobstr])
    r = requests.get(URI, headers={
        'Authorization': 'Bearer %s' % token,
    }).json()
    return r
