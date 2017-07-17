# drchrono Hackathon

Hello DrChrono! I believe I've completed the task you sent me.

Please see models.py, urls.py, views.py, and templates/auth.html for major changes. If you have any questions, please email at noelle.d.anthony AT gmail.com.

### TODO
- Uncomment the section in views.py that actually emails the patients (see comment for details)
- Format output (should match general practice site formatting)
- Add columns to patient data indicating when email has been sent, so nobody gets a double
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
