from django.conf.urls import handler404, handler500
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from car.views import *
from kolesa import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('', IndexView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', sign_out, name="logout"),
    path('<slug:slug>/<slug:url>/', carShow, name='show'),
    path('<slug:slug>/', CategoryCars.as_view(), name='category'),

]

handler404 = myHandler404
handler500 = myHandler500

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
