from django.urls import path
from main import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

urlpatterns = [
    path("", views.loginPage, name="login"),  
    path("quizview", views.Quiz_view, name="quizview"),
    path("test_completed", views.test_comp , name = "test_completed"),
    path('register', views.registerPage, name="register"),
	path('logout', views.logoutUser, name="logout"),


]
urlpatterns += staticfiles_urlpatterns()
