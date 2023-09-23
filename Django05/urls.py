"""
URL configuration for Django05 project.

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
from bdmodels import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add1/',views.add1, name='add1'),
    path('',views.index, name='home'),
    path('create/',views.create, name='create'),
    path('del/<int:ids>', views.delete, name='del'),
    path('edit/<int:ids>', views.edit, name='edit'),

]
'''
DB БД база данных
СУБД система управления БД
ORM переходник между питон-СУБД

Для создания таблиц есть методы - save, create
удаление - delete
поиск - all, get, filter, exclude
CRUD

связи:
один ко многим 
многие ко многим
один к одному
'''
