from django.urls import path

from . import views

app_name = "dl"

urlpatterns = [
    path("", views.survey_view, name="survey_view"),
    path("query/", views.survey_query, name="survey_query"),
    
     ]