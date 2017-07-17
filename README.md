# drchrono Hackathon

Hello DrChrono! I believe I've completed the task you sent me.

Please see models.py, urls.py, views.py, and templates/auth.html for major changes. If you have any questions, please email at noelle.d.anthony AT gmail.com.

I've chosen to focus on the back end of this project; as a general-purpose tool, the front end should be styled to the preference of the practice using the tool. I have, however, used Bootstrap for the front end to make it easier to view as a testbed and to incorporate into other designs.

The section that actually sends the email is commented out and must be re-enabled in order to function properly. I noticed that at least one patient in the test database had an email address from a non-drchrono.com source, and it wasn't clear whether that address was live; it seemed unwise to send email to a non-vetted address. If the addresses in the test database are all vetted, the section can safely be uncommented.

In a best-case scenario the database would be modified to include a column indicating that a birthday email has been sent, so that if this code is run more than once on a given day, it won't send emails more than once. I wasn't sure if I was allowed to modify the test database, so I didn't include this, although the code does include a commented-out test to see if that column is set. The code should also reset that column to false every time the year changes (i.e. on January 1).

Selecting the doctor's name and email is not as clever as I'd like, but it gets the job done. Also: I don't see a way to access the overall practice's name or a general email address in the API. There are ways to identify individual offices, but as a patient can visit multiple offices in a practice and there doesn't seem to be a way to reliably determine which is most recent, I can't use that as a point of reference.

### TODO
- Uncomment the section in views.py that actually emails the patients (see above for details)
- Format output (should match general practice site formatting)
- Add columns to patient data indicating when email has been sent, so nobody gets an email twice
- Reset those columns on 1/1 of each year

## Original readme below

### Requirements
- [pip](https://pip.pypa.io/en/stable/)
- [python virtual env](https://packaging.python.org/installing/#creating-and-using-virtual-environments)

### Setup
``` bash
$ pip install -r requirements.txt
$ python manage.py runserver
```

`social_auth_drchrono/` contains a custom provider for [Python Social Auth](http://psa.matiasaguirre.net/) that handles OAUTH for drchrono. To configure it, set these fields in your `drchrono/settings.py` file:

```
SOCIAL_AUTH_DRCHRONO_KEY
SOCIAL_AUTH_DRCHRONO_SECRET
SOCIAL_AUTH_DRCHRONO_SCOPE
LOGIN_REDIRECT_URL
```
