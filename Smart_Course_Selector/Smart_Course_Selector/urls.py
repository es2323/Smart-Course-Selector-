"""
URL configuration for Smart_Course_Selector project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from quiz.views import index, start_quiz, quiz

urlpatterns = [
    path('', index, name='index'),  # Home page
    path('admin/', admin.site.urls),
    path('quiz/', start_quiz, name='start_quiz'),  # Default redirect for /quiz/
    path('quiz/<int:session_id>/', quiz, name='quiz_with_session'),  # Quiz for a specific session
]






