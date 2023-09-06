from django.urls import path
from .api_views import SurveyViewset, fetch_survey_data, create_survey, register_visit, top_five_weekly_voivodeships, top_five_monthly_voivodeships, number_of_all_surveys, number_of_top5monthly_surveys, number_of_top5weekly_surveys
from . import views

app_name = "dl"

urlpatterns = [
    path("", views.survey_view, name="survey_view"),
    path("query/", views.survey_query, name="survey_query"),
    path("top_voivodships/", views.top_voivodships, name="top_voivodships"),
    path('api/v1/top5weekly/', top_five_weekly_voivodeships, name='top_five_weekly_voivodeships'),
    path('api/v1/top5monthly/', top_five_monthly_voivodeships, name='top_five_monthly_voivodeships'),
    path('api/v1/all_count', number_of_all_surveys, name='number_of_all_surveys'),
    path('api/v1/top5_weekly_count', number_of_top5weekly_surveys, name='number_of_top5weekly_surveys'),
    path('api/v1/top5_monthly_count', number_of_top5monthly_surveys, name='number_of_top5monthly_surveys'),
    path('api/v1/register-visit/', register_visit, name='register_visit'),
    path('api/v1/create-survey/', create_survey, name='create-survey'),
    path('fetch_survey_data/', fetch_survey_data, name='fetch_survey_data'),
    
     ]