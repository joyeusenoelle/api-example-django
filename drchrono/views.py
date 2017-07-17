# Create your views here.
from django.shortcuts import render
import requests, ast, datetime
from django.db import connection

from models import fetch_drchrono_userdata, send_birthday_mail

def get_users(request):
    """
    Fetches users born on the current date and sends them a birthday email.
    Parameters:
    * request: a Django request
    """
    practice = {
        'name': "Noelle's Medical Clearinghouse",
        'email': 'example@example.com',
    }
    today = datetime.date.today()
    todaystr = today.strftime('%Y-%m-%d')
    targetdate = todaystr
    r = fetch_drchrono_userdata(targetdate)
# This section is commented out because some users in the sample data
# have what appear to be valid email addresses and we'd prefer not to
# send them unexpected emails from testing practices.
#    if r:
#        for row in r:
#            mail_message = send_birthday_mail(
#                               patient_fname  = row['first_name'],
#                               patient_email  = row['email'],
#                               practice_name  = practice['name'],
#                               practice_email = practice['email'],
#                               doctor_name    = "Anthony"
#                               )
#            row['message'] = mail_message
    return render(request, 'auth.html',
        {'response': r,
    })
