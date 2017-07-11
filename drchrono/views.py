# Create your views here.
from django.shortcuts import render
import requests, ast
from django.db import connection

BASE_URL = "https://drchrono.com"

def get_users(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, extra_data from social_auth_usersocialauth")
        row = cursor.fetchone()
    token = ast.literal_eval(row[1])['access_token']
    r = requests.get(BASE_URL + '/api/patients', headers={
        'Authorization': 'Bearer %s' % token,
    }).json()
    return render(request, 'auth.html',
        {'response': r,
         'row': row,
         'token': token,
        })
