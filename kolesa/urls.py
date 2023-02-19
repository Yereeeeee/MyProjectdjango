
from django.conf.urls import handler404, handler500
from django.contrib import admin
from django.urls import path

from kolesa.car.views import myHandler404, myHandler500

urlpatterns = [
    path('admin/', admin.site.urls),
]

handler404 = myHandler404
handler500 = myHandler500
