from django.conf.urls import handler404, handler500
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.views.decorators.cache import cache_page
from car.views import *
from kolesa import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('', cache_page(60)(IndexView.as_view()), name='index'),
    path('register/', RegisterView.as_view(), name="register"),
    path('api/auth/', include('rest_framework.urls')),
    path('login/', Login.as_view(), name="login"),
    path('logout/', sign_out, name="logout"),
    path('show/<slug:slug>/<slug:url>/', carShow, name='show'),
    path('category/<slug:slug>/', CategoryCars.as_view(), name='category'),

]

handler404 = myHandler404
handler500 = myHandler500

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
