from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dl.models import Survey, Visit
from dl.serializers import SurveySerializer, SurveyTopFiveSerializer, VisitSerializer
from django.db.models import Count
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from django.utils import timezone
from rest_framework import status

class SurveyViewset(ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

  
    

@api_view(['GET'])
def top_five_weekly_voivodeships(request):
    # Query the database to get the top 5 voivodeships with the highest number of surveys

    # Calculate the date 7 days ago from today
    seven_days_ago = timezone.now() - timedelta(days=7)

    top_5_weekly_voivodeships = Survey.objects.filter(timestamp__gte=seven_days_ago).values('voivodship').annotate(survey_count=Count('voivodship')).order_by('-survey_count')[:5]
    # Serialize the aggregated data using the SurveyTopFiveSerializer
    serializer = SurveyTopFiveSerializer(top_5_weekly_voivodeships, many=True)

    # Return the response
    return Response(serializer.data)

@api_view(['GET'])
def top_five_monthly_voivodeships(request):
    # Calculate the date one month ago from today
    one_month_ago = timezone.now() - relativedelta(months=1)

    # Query the database to get the top 5 voivodeships with the highest number of surveys submitted within the last month
    top_5_monthly_voivodeships = Survey.objects.filter(timestamp__gte=one_month_ago).values('voivodship').annotate(survey_count=Count('voivodship')).order_by('-survey_count')[:5]
    print(top_5_monthly_voivodeships)
    # Serialize the aggregated data using the SurveyTopFiveSerializer
    serializer = SurveyTopFiveSerializer(top_5_monthly_voivodeships, many=True)
    
    # Return the response
    return Response(serializer.data)


@api_view(['GET'])
def number_of_all_surveys(request):
    number = Survey.objects.count()
    # Create a dictionary with the count and include it in the response
    response_data = {
        'count': number
    }

    return Response(response_data)

@api_view(['GET'])
def number_of_top5weekly_surveys(request):
    seven_days_ago = timezone.now() - timedelta(days=7)

    number = len(Survey.objects.filter(timestamp__gte=seven_days_ago).values('id','voivodship').annotate(survey_count=Count('voivodship')).order_by('-survey_count')[:5])
    # Create a dictionary with the count and include it in the response
    response_data = {
        'count': number
    }

    return Response(response_data)

@api_view(['GET'])
def number_of_top5monthly_surveys(request):
    one_month_ago = timezone.now() - relativedelta(months=1)
    number = len(Survey.objects.filter(timestamp__gte=one_month_ago).values('id', 'voivodship').annotate(survey_count=Count('voivodship')).order_by('-survey_count')[:5])
    # Create a dictionary with the count and include it in the response
    response_data = {
        'count': number
    }

    return Response(response_data)


@api_view(['GET'])
def register_visit(request):
    visit, created = Visit.objects.get_or_create(pk=1)
    if created:
        print("New Visit object was created.")
    else:
        print("Using existing Visit object.")
    visit.count += 1
    visit.save()
    
    serializer = VisitSerializer(visit)
    return Response(serializer.data)


@api_view(['POST'])
def create_survey(request):
    if request.method == 'POST':
        serializer = SurveySerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def fetch_survey_data(request):
    if request.method == 'POST':
        age = request.data.get('age')
        gender = request.data.get('gender')
        voivodship = request.data.get('voivodship')
        city_size = request.data.get('city_size')
        group = request.data.get('group')

        # Query the database for matching data
        matched_data = Survey.objects.filter(
            age=age, 
            gender=gender, 
            voivodship=voivodship,
            city_size=city_size,
            group=group
        )

        # Serialize the data for the response
        
        serialized_data = SurveySerializer(matched_data, many=True).data

        return Response(serialized_data, status=status.HTTP_200_OK)

    return Response({"detail": "Invalid request method."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
