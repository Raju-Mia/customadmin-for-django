from django.urls import path
from .views import *

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', admin_login, name='admin_login'),
    path('dashboard/', admindashboard, name='admindashboard'),

    # path('login/', auth_views.admin_login.as_view(
    #     template_name='customadmin/login.html'
    #     ), 
    #     name='login'
    # ),

    path('logout/', auth_views.LogoutView.as_view(
        template_name='customadmin/logout.html'
        ), 
        name='logout'
    ),
]