# Create your views here.
from django.shortcuts import render
import requests, ast, datetime
from django.db import connection

from models import fetch_drchrono_userdata

def get_users(request):
    today = datetime.date.today()
    todaystr = today.strftime('%Y-%m-%d')
    targetdate = ''#'1979-08-01'
    r = fetch_drchrono_userdata(targetdate)
    return render(request, 'auth.html',
        {'response': r,
        })
