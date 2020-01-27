from django.urls import path
from django.contrib.auth import views 
from signup.views import register
from .views import login_view
from usersprofile.views import profile
urlpatterns = [
    path('',views.LoginView.as_view(template_name = 'login.html'),name= 'login'),
    path('',register,name ='signup'),
]