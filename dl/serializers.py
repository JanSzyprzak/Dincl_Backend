from rest_framework import serializers
from .models import Survey

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'


class SurveyTopFiveSerializer(serializers.Serializer):
    voivodship = serializers.CharField()
    survey_count = serializers.IntegerField()

    