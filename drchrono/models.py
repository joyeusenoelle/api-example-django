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
    response = r['results']
    # Response is paginated, so keep loading until it stops giving URIs
    while r['next'] != None:
        r = requests.get(r['next'], headers={
            'Authorization': 'Bearer %s' % token,
        }).json()
        response.append(r['results'])
    DOC_URI = "".join([BASE_URL,
                       '/api/doctors',
                       ''])
    doc_r = requests.get(DOC_URI, headers={
        'Authorization': 'Bearer %s' % token,
    }).json()
    doctors = r['results']
    doc_names = {}
    doc_emails = {}
    for doc in doctors:
        doc_names[doc['id']] = doc['last_name']
        doc_emails[doc['id']] = doc['email']
    for line in results:
        d_id = line['doctor']
        line['doctor'] = doc_names[d_id]
        line['doc_email'] = doc_emails[d_id]
    return response

def send_birthday_mail(patient_fname, patient_email, practice_email, doctor_name=None):
    """
    Sends the birthday email.
    arguments:
    * patient_fname = the patient's first name (str, required)
    * patient_email = the patient's email address (str, required)
    * doctor_email = the email address of the doctor (str, required)
    * doctor_name = the patient's primary doctor's last name (str, optional)
    """
    text_full = "Dr. {} would like to wish you a very happy birthday and many happy returns of the day!".format(doctor_name)
    email_body = "Dear {},\n\n{}\n\nSee you soon!".format(
        patient_fname,
        text_full
    )
    try:
        send_mail(
            'Happy birthday from Dr. {}!'.format(doctor_name),
            email_body,
            practice_email,
            [patient_email],
            fail_silently=False,
        )
        return {'code':0, 'message': "Mail sent successfully."}
    except Exception as e:
        msg = "Could not send mail ({}): {}".format(e.errno, e.strerror)
        return {'code':-1, 'message': msg }
