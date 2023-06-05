from django import forms
from .models import Survey  # Import the Survey model

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['age', 'gender', 'voivodship', 'city_size', 'group', 'identification_with_group', 'identification_with_minority', 'group_diversity', 'ease_of_joining', 'rule_fairness', 'minority_participation_in_life', 'minority_participation_in_decisions', 'minority_potential_utilization', 'personal_security_feeling', 'minority_security_feeling']


class SurveyQueryForm(forms.Form):
    age = forms.ChoiceField(choices=Survey.AGE_CHOICES, required=False)
    gender = forms.ChoiceField(choices=Survey.GENDER_CHOICES, required=False)
    voivodship = forms.ChoiceField(choices=Survey.VOIVODSHIP_CHOICES, required=False)
    city_size = forms.ChoiceField(choices=Survey.CITY_SIZE_CHOICES, required=False)
    group = forms.ChoiceField(choices=Survey.GROUP_CHOICES, required=False)
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'text', 'class': 'datepicker'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'text', 'class': 'datepicker'}))

