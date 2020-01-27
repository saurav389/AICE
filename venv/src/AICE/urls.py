"""AICE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views 
from django.conf.urls.static import static
from django.urls import path, include
from Home.views import home_view
from login.views import login_view
from signup.views import register
from Blogs.views import blogs_view
from contactus.views import contact_view
from about.views import about_view


urlpatterns = [
    path('',home_view,name='Home'),
    path('profile/',include('usersprofile.urls')),
    path('login/',include('login.urls')),
    path('signup/',include('signup.urls')),
    path('logout/',views.LogoutView.as_view(template_name = 'logout.html'),name = 'logout'),
    path('blogs/',blogs_view),
    path('contactus/',contact_view),
    path('about/',about_view),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
