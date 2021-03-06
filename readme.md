# Room Booker

## Install
1. Run docker container with Postgres
```
$ docker run --name postgres-docker -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
```
2. Create `local_settings.py` in core app and fill it up with configuration e.g.
```
SECRET_KEY = "yoursecretkey:)"
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'localhost',
            'PORT': '5432',
            }
        }

```
3. Install requirements:
```
pip3 install -r requirements.txt
```
if psycopg cause problems then try:
```
pip install psycopg2-binary
```

4. Migrate database
```
./manage.py migrate
```

## Development Tips
1. Please create new templates in the following way:

```
{% extends 'template.html' %}

{% block content %}
  twój kod html
  twój kod html
  albo jakieś pętle djangowe
{% endblock %}
```

2. Libraries

  * awesomeicons 4.8

    - icons: https://fontawesome.com/v4.7.0/icons/

    - sample use: `<i class="fa fa-thumbs-up" aria-hidden="true"></i>`
    
 
  * bootstrap 4.4.1

    - documentation: https://getbootstrap.com/docs/4.0/getting-started/introduction/
    
  * dropzone 5.7.0

    - documentation: https://www.dropzonejs.com/
    

