from django.urls import path
from . import views



urlpatterns=[
    path('login/',views.login_user,name='logi'),
    path('logout/',views.logout_user,name='logo'),
    path('dashboard/',views.dashboard,name='dash'),
]