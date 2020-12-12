"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# from users.views import auto_login
from randomise.views import randomise_teams, welcome, create_teams, set_teams
# from .error_handling import customhandler404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='welcome'),
    path('create_teams/', create_teams, name='create_teams'),
    path('set_teams/<str:number>/<str:name>/<str:team_size>/', set_teams, name='set_teams'),
    path('randomise/<str:name>/', randomise_teams, name='randomise_teams'),
    # path('goTeam', auto_login, name='auto_login'),
]

# handler404 = 'error_handling.customhandler404'
