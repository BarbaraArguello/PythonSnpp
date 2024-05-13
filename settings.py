# Static files (CCS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/hoeto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (os.path.join(Base_DIR,'sistema2/static'),)

from pathlib import Path
import os

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': ['C:/Users/#copiar la ruta de los templates# '],
    'APP_DIRS': True,
    'OPTIONS':{
      'context_processors':[],
