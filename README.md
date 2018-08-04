# Django interact with MercadoLibreAPI (Login & Create|List products)

A django app that interact with MercadoLibre api  https://developers.mercadolibre.com/en_us/api-docs .


## Functionality

- Log in 
- Sing Up
- MercadoLibre outh
- Create a publication of an particular product .- 
- List your active publications .
- Log out
- Multilingual: English, Spanish



## Installing

### Clone the project

```
git clone https://github.com/franbonafina/djangoMercadoLibre
cd djangoMercadoLibre
```

## Local steps
```
pip install django==2.7

cd meli-python
python setup.py install

cd ..

python source/manage.py migrations
python source/manage.py runserver
```

### Install dependencies & activate virtualenv

```
pip install pipenv

pipenv install
pipenv shell

python meli-pythonSDK/setup.py install
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
