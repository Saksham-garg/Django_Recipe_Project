"""
URL configuration for django_tut project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from home.views import *
from veges.views import *
from django.conf.urls.static import static
from django.conf import settings
from accounts.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('delete-recipe/<id>',deleteRecipe,name='deleteRecipe'),
    path('update-recipe/<id>',updateRecipe,name='updateRecipe'),
    path('recipes/',recipes,name='recipes'),
    path('login_page/',login_page,name='login_page'),
    path('logout_page/',logout_page,name='logout_page'),
    path('Register/',Register,name='Register'),
    path('',home,name = 'home'),
    path('about/',about,name='about'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()