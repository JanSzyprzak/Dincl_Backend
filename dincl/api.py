from rest_framework import routers
from dl import api_views as survey_views

router = routers.DefaultRouter()
router.register('dl', survey_views.SurveyViewset)