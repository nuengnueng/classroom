from django.urls import path
from classroom import views


urlpatterns = [
     path('', views.home, name="home"),
     path('./classroom/home', views.home, name="home"),
     path('stream', views.stream, name="stream"),
     path('classwork', views.classwork, name="classwork"),
     path('people', views.people, name="people"),
     path('grade', views.grade, name="grade"),
     path('menu', views.menu, name="menu"),
]
