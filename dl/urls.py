from django.urls import path
from .api_views import SurveyViewset, top_five_weekly_voivodeships
from . import views

app_name = "dl"

urlpatterns = [
    path("", views.survey_view, name="survey_view"),
    path("query/", views.survey_query, name="survey_query"),
    path("top_voivodships/", views.top_voivodships, name="top_voivodships"),
    path('top5/', top_five_weekly_voivodeships, name='top_five_voivodeships'),
    
     ]