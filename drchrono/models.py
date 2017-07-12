from django.db import models, connection
from django.core.mail import send_mail
import ast, requests
# Create your models here.

BASE_URL = "https://drchrono.com"

def fetch_drchrono_userdata(dob = None):
    """
    Gets user data from DrChrono's patients API
    arguments:
    * dob = "YYYY-MM-DD" (str, optional)
      If supplied, will fetch all patients with that birthday
      If not supplied, will fetch all patients
    """
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

def send_birthday_mail(patient_fname, patient_email, practice_name, practice_email, doctor_name=None):
    """
    Sends the birthday email.
    arguments:
    * patient_fname = the patient's first name (str, required)
    * patient_email = the patient's email address (str, required)
    * practice_name = the name of the practice (str, required)
    * practice_email = the email address of the practice (str, required)
    * doctor_name = the patient's primary doctor's last name (str, optional)
    """
    if doctor_name in [None, '']:
        text_start = "A"
    else:
        text_start = "Dr. {} and a".format(doctor_name)
    text_full = "{}ll of us here at {} want to wish you a very happy birthday and many happy returns of the day!".format(text_start,practice_text)
    email_body = "Dear {},\n\n{}\n\nSee you soon!\n\n{}".format(
        patient_fname,
        text_full,
        practice_name
    )
    try:
        send_mail(
            'Happy birthday from {}!'.format(practice_name),
            email_body,
            practice_email,
            [patient_email],
            fail_silently=False,
        )
        return "Mail sent successfully."
    except SMTPException as e:
        return "Could not send mail ({}): {}".format(e.errno, e.strerror)
