from django.urls import path
from django.contrib.auth import views 
from .views import registration_view, EmployeeList, EmployeeDelete, EmployeeRateView

urlpatterns = [
    path('',registration_view,name ='register'),
    path('<int:id>/',registration_view,name ='update'),
    path('delete/<int:id>/',EmployeeDelete,name ='delete'),
    path('list/',EmployeeList,name ='list'),
    path('rate/',EmployeeRateView,name='rate')

]

