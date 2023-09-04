from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Survey(models.Model):
    AGE_CHOICES = [("<18", _("<18")), ("18-40", _("18-40")), ("41-60", _("41-60")), (">60", _(">60"))]
    GENDER_CHOICES = [("K", _("K")), ("M", _("M")), ("Nie chcę podać", _("Nie chcę podać"))]
    CITY_SIZE_CHOICES = [("małe", _("małe")), ("średnie", _("średnie")), ("duże", _("duże"))]
    VOIVODSHIP_CHOICES = [("dolnośląskie", _("dolnośląskie")), ("kujawsko-pomorskie", _("kujawsko-pomorskie")), ("lubelskie", _("lubelskie")), ("lubuskie", _("lubuskie")), ("łódzkie", _("łódzkie")), ("małopolskie", _("małopolskie")), ("mazowieckie", _("mazowieckie")), ("opolskie", _("opolskie")), ("podkarpackie", _("podkarpackie")), ("podlaskie", _("podlaskie")), ("pomorskie", _("pomorskie")), ("śląskie", _("śląskie")), ("świętokrzyskie", _("świętokrzyskie")), ("warmińsko-mazurskie", _("warmińsko-mazurskie")), ("wielkopolskie", _("wielkopolskie")), ("zachodniopomorskie", _("zachodniopomorskie"))]

    age = models.CharField(max_length=5, choices=AGE_CHOICES, verbose_name=_('Wiek'))
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES, verbose_name=_('Płeć'))
    voivodship = models.CharField(max_length=30, choices=VOIVODSHIP_CHOICES, verbose_name=_('Województwo'))
    city_size = models.CharField(max_length=7, choices=CITY_SIZE_CHOICES, verbose_name=_('Miasto'))

    GROUP_CHOICES = [("Moi znajomi", _("Moi znajomi")), ("Moi koledzy/koleżanki w szkole/na uczelni", _("Moi koledzy/koleżanki w szkole/na uczelni")), ("Moja praca", _("Moja praca")), ("Mój region", _("Mój region")), ("Mój kraj", _("Mój kraj"))]
    group = models.CharField(max_length=50, choices=GROUP_CHOICES, verbose_name=_('Wybór ocenianej grupy'))

    RATING_CHOICES = [(i, str(i)) for i in range(1, 11)] 
    identification_with_group = models.IntegerField(choices=RATING_CHOICES, verbose_name=_('Twoja identyfikacja z wybraną grupą'))
    identification_with_minority = models.IntegerField(choices=RATING_CHOICES, verbose_name=_('Twoja identyfikacja z mniejszością/mniejszościami w wybranej grupie'))
    group_diversity = models.IntegerField(choices=RATING_CHOICES, verbose_name=_('Zróżnicowanie wybranej grupy'))
    ease_of_joining = models.IntegerField(choices=RATING_CHOICES, verbose_name=_('Łatwość dołączenia do wybranej grupy'))
    rule_fairness = models.IntegerField(choices=RATING_CHOICES, verbose_name=_('Uczciwość zasad w wybranej grupie'))
    minority_participation_in_life = models.IntegerField(choices=RATING_CHOICES, verbose_name=_('Uczestniczenie mniejszości w życiu wybranej grupy'))
    minority_participation_in_decisions = models.IntegerField(choices=RATING_CHOICES, verbose_name=_('Uczestniczenie mniejszości w decyzjach wybranej grupy'))
    minority_potential_utilization = models.IntegerField(choices=RATING_CHOICES, verbose_name=_('Wykorzystanie potencjału mniejszości w wybranej grupie'))
    personal_security_feeling = models.IntegerField(choices=RATING_CHOICES, verbose_name=_('Twoje poczucie bezpieczeństwa w wybranej grupie'))
    minority_security_feeling = models.IntegerField(choices=RATING_CHOICES, verbose_name=_('Poczucie bezpieczeństwa mniejszości w wybranej grupie'))

    #timestamp = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(default=timezone.now)


class Visit(models.Model):
    count = models.IntegerField(default=0)