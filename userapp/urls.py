from django.urls import path
from userapp import views

urlpatterns=[ 
    path("register",views.register,name="new_member"),
    path("login",views.login,name="login"),
    path("logout",views.login,name="logout"),
]