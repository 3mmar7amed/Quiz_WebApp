from django.urls import path
from main import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

urlpatterns = [
    path("", views.loginPage, name="login3"),  
    path("quizview", views.Quiz_view, name="quizview"),
    path("test_completed", views.test_comp , name = "test_completed"),
    path('register', views.registerPage, name="register"),
	path('logout', views.logoutUser, name="logout"),
    path('user_exams' , views.user_lastExams , name = "user_exams"),


]
urlpatterns += staticfiles_urlpatterns()
