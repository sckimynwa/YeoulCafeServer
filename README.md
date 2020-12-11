# YeoulCafeServer

### Installation

1. Create Virtual Environment (python3 must be installed)

```
python3 -m venv env       // create your virtual environment
source env/bin/activate   // activate your virtual environment
pip3 install django djangorestframework
sudo pip3 install pylint pylint-django

```

2. Migrate Any Changes

```
python3 manage.py makemigrations
python3 manage.py migrate
```

3. Run Server

```
python3 manage.py runserver
```

### Adding Models & APIs

1. Create App

```
python3 manage.py startapp (your app name)
```

2. Migrate Any Changes

```
python3 manage.py makemigrations
python3 manage.py migrate
```
