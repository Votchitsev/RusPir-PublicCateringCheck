# Generated by Django 4.1 on 2023-10-11 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checks', '0002_employeeposition_employeepositionquestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='relational_question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_question', to='checks.question'),
        ),
    ]