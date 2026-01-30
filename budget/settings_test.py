from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test_db',          
        'USER': 'test_user',        
        'PASSWORD': 'test_pass',    
        'HOST': '127.0.0.1',        
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        },
    }
}