# Simple Django Login and Registration

An example of Django project with basic user functionality.


## Functionality

- Log in
    - via username & password
    - via email & password
    - via email or username & password
    - with a remember me checkbox (optional)
- Create an account
- Log out
- Profile activation via email
- Reset password
- Remind a username
- Resend an activation code
- Change password
- Change email
- Change profile
- Multilingual: English, Spanish


## Installing

### Clone the project

```
git clone https://github.com/egorsmkv/simple-django-login-and-register
cd simple-django-login-and-register
```

### Install dependencies & activate virtualenv

```
pip install pipenv

pipenv install
pipenv shell
```

### Apply migrations

```
python source/manage.py migrate
```

### Running
#### Just run this command:
```
python source/manage.py runserver
```
