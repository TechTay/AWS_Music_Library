# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j((u)ws9)^d_sbga^cizvr%ged3d2d0t46*9=5d$)al(s@v_6c'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'Music_Library_db',
        'USER': 'admin',
        'PASSWORD': 'Bigboyin!1',
        'HOST':'musiclibrary.cfoflavo0ggo.us-east-1.rds.amazonaws.com',
        'PORT': '3306',
    }
}