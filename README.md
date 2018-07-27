# Login with Django authorize by MercadoLibre and interact with the API

A django app that interact with MercadoLibre api  https://developers.mercadolibre.com/en_us/api-docs .


## Functionality

- Log in (MercadoLibre credentials outh)
- Create a publication of an particular product .
- Handle errors .
- List your active publications .
- Log out
- Create an account
- Change password & Resend an activation code
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
