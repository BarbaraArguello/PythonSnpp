from django.urls import path
from django.contrib import admin
from sistema2.views import *

urlpatterns = [
  path('admin/', admin.site.urls),
  path('hoy/', fecha_hora),
  path('ver/<int:num>', consultar),
  path('index/', plantilla_index),
  path('login/', plantilla_login),
]
