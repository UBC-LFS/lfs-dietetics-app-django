# lfs-dietetics-app-django

## Installation
```
pip install virtualenv
virtualenv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create a .env file
```
DB_HOST=
DB_USER=
DB_PASS=
DB_NAME=
PORT=
```

## Running the app
```
venv\Scripts\activate # unless it is already activated
cd dieteticsProject
py manage.py runserver
```