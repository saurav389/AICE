from django.urls import path
from django.contrib.auth import views 
from .views import profile

urlpatterns = [
    path('',profile,name ='profile'),
    path('',views.LogoutView.as_view(),name = 'logout'),
]

