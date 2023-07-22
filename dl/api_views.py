from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dl.models import Survey
from dl.serializers import SurveySerializer, SurveyTopFiveSerializer
from django.db.models import Count
from datetime import datetime, timedelta

class SurveyViewset(ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

    """@action(detail=False, methods=['GET'])
    def top_five_voivodeships(request):
        # Query the database to get the top 5 voivodeships with the highest number of surveys
        top_voivodeships = Survey.objects.values('voivodship').annotate(survey_count=Count('voivodship')).order_by('-survey_count')[:5]

        # Serialize the data using the same SurveySerializer
        serializer = SurveySerializer(top_voivodeships, many=True)

        # Return the response
        return Response(serializer.data)"""
    
    

@api_view(['GET'])
def top_five_weekly_voivodeships(request):
    # Query the database to get the top 5 voivodeships with the highest number of surveys

    # Calculate the date 7 days ago from today
    seven_days_ago = datetime.now() - timedelta(days=7)

    top_5_weekly_voivodeships = Survey.objects.filter(timestamp__gte=seven_days_ago).values('voivodship').annotate(survey_count=Count('voivodship')).order_by('-survey_count')[:5]
    # Serialize the aggregated data using the SurveyTopFiveSerializer
    serializer = SurveyTopFiveSerializer(top_5_weekly_voivodeships, many=True)

    # Return the response
    return Response(serializer.data)