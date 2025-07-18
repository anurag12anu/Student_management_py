from django.urls import path
from . import views



urlpatterns=[
    path('login/',views.login_user,name='logi'),
    path('logout/',views.logout_user,name='logo'),
    
    path('dashboard/',views.dashboard,name='dash'),
    path('add/',views.student_add,name='st_add'),
    path('update/<int:pk>/',views.student_update,name='st_update'),
    path('delete/<int:pk>/', views.student_delete,name='st_delete'),
    
]