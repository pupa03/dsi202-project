# dsi202-project

require
mySQL, mySQL workbench, pipenv

## Change Databases
```
> settings.py

# DATABASE

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'yourdatabasesname',
        'USER': 'root',
        'PASSWORD': 'yourdatabasepassword',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}

```

```
> settings.py

# Email

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = 'your@email'
#EMAIL_HOST_PASSWORD = 'passwordforapp'
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True
#EMAIL_USE_SSL = False

# Email for test -> ./test_inbox
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = BASE_DIR/"test_inbox"
PASSWORD_RESET_TIMEOUT = 300
```

## Setup
```
pipenv install
```
Connect databases

```
pipenv shell
```
```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
