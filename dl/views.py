
# Create your views here.
from django.shortcuts import render
from .forms import SurveyForm, SurveyQueryForm
from django.db.models import Avg
from .models import Survey




def survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'dl/success.html') 
    else:
        form = SurveyForm()

    return render(request, 'dl/survey.html', {'form': form})



def survey_query(request):
    if request.method == 'POST':
        form = SurveyQueryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            filters = {k: v for k, v in data.items() if v is not None and k not in ['start_date', 'end_date']}

            surveys = Survey.objects.filter(**filters)
            
            if data.get('start_date') and data.get('end_date'):
                surveys = surveys.filter(timestamp__range=[data['start_date'], data['end_date']])

            averages = {
                key: (value or 0)
                for key, value in surveys.aggregate(
                    avg_identification_with_group=Avg('identification_with_group'),
                    avg_identification_with_minority=Avg('identification_with_minority'),
                    avg_group_diversity=Avg('group_diversity'),
                    avg_ease_of_joining=Avg('ease_of_joining'),
                    avg_rule_fairness=Avg('rule_fairness'),
                    avg_minority_participation_in_life=Avg('minority_participation_in_life'),
                    avg_minority_participation_in_decisions=Avg('minority_participation_in_decisions'),
                    avg_minority_potential_utilization=Avg('minority_potential_utilization'),
                    avg_personal_security_feeling=Avg('personal_security_feeling'),
                    avg_minority_security_feeling=Avg('minority_security_feeling'),
                ).items()
            }

            return render(request, 'dl/results.html', {'averages': averages})

    else:
        form = SurveyQueryForm()

    return render(request, 'dl/query.html', {'form': form})















