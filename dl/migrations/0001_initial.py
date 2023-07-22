# Generated by Django 4.2.1 on 2023-06-02 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(choices=[('<18', '<18'), ('18-40', '18-40'), ('41-60', '41-60'), ('>60', '>60')], max_length=5, verbose_name='Wiek')),
                ('gender', models.CharField(choices=[('K', 'K'), ('M', 'M'), ('Nie chcę podać', 'Nie chcę podać')], max_length=15, verbose_name='Płeć')),
                ('voivodship', models.CharField(choices=[('dolnośląskie', 'dolnośląskie'), ('kujawsko-pomorskie', 'kujawsko-pomorskie'), ('lubelskie', 'lubelskie'), ('lubuskie', 'lubuskie'), ('łódzkie', 'łódzkie'), ('małopolskie', 'małopolskie'), ('mazowieckie', 'mazowieckie'), ('opolskie', 'opolskie'), ('podkarpackie', 'podkarpackie'), ('podlaskie', 'podlaskie'), ('pomorskie', 'pomorskie'), ('śląskie', 'śląskie'), ('świętokrzyskie', 'świętokrzyskie'), ('warmińsko-mazurskie', 'warmińsko-mazurskie'), ('wielkopolskie', 'wielkopolskie'), ('zachodniopomorskie', 'zachodniopomorskie')], max_length=30, verbose_name='Województwo')),
                ('city_size', models.CharField(choices=[('małe', 'małe'), ('średnie', 'średnie'), ('duże', 'duże')], max_length=7, verbose_name='Miasto')),
                ('group', models.CharField(choices=[('Moi znajomi', 'Moi znajomi'), ('Moi koledzy/koleżanki w szkole/na uczelni', 'Moi koledzy/koleżanki w szkole/na uczelni'), ('Moja praca', 'Moja praca'), ('Mój region', 'Mój region'), ('Mój kraj', 'Mój kraj')], max_length=50, verbose_name='Wybór ocenianej grupy')),
                ('identification_with_group', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], verbose_name='Twoja identyfikacja z wybraną grupą')),
                ('identification_with_minority', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], verbose_name='Twoja identyfikacja z mniejszością/mniejszościami w wybranej grupie')),
                ('group_diversity', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], verbose_name='Zróżnicowanie wybranej grupy')),
                ('ease_of_joining', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], verbose_name='Łatwość dołączenia do wybranej grupy')),
                ('rule_fairness', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], verbose_name='Uczciwość zasad w wybranej grupie')),
                ('minority_participation_in_life', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], verbose_name='Uczestniczenie mniejszości w życiu wybranej grupy')),
                ('minority_participation_in_decisions', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], verbose_name='Uczestniczenie mniejszości w decyzjach wybranej grupy')),
                ('minority_potential_utilization', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], verbose_name='Wykorzystanie potencjału mniejszości w wybranej grupie')),
                ('personal_security_feeling', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], verbose_name='Twoje poczucie bezpieczeństwa w wybranej grupie')),
                ('minority_security_feeling', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], verbose_name='Poczucie bezpieczeństwa mniejszości w wybranej grupie')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]