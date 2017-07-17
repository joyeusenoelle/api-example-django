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
    today = datetime.date.today()
    todaystr = today.strftime('%Y-%m-%d')
    targetdate = todaystr
    # The practice set is fairly small and has few valid birthdays.
    # To test, uncomment this line, which will return a single user:
    # targetdate = '1979-08-01'
    r = fetch_drchrono_userdata(targetdate)
# This section is commented out because some users in the sample data
# have what appear to be valid email addresses and we'd prefer not to
# send them unexpected emails from testing practices.
#    if r:
#        for row in r:
#            # Uncomment the last term when the 'bday_email_sent' column has been added to the db
#            if row['first_name'] and row['email']:# and (not row['bday_email_sent']):
#                mail_message = send_birthday_mail(
#                                   patient_fname  = row['first_name'],
#                                   patient_email  = row['email'],
#                                   doctor_email   = row['doc_email'],
#                                   doctor_name    = row['doctor']
#                                   )
#                row['message'] = mail_message
#            else:
#                row['message'] = "No email sent."
    return render(request, 'auth.html',
        {'response': r,
    })
