# Generated by Django 4.1 on 2023-10-09 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ControlEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата проверки')),
                ('revizor', models.CharField(max_length=100, null=True)),
                ('score', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CorrectionReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_given', models.BooleanField(verbose_name='Отчет представлен')),
                ('has_completed', models.BooleanField(verbose_name='Отчёт отработан')),
                ('control_event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='correction_report', to='checks.controlevent')),
            ],
        ),
        migrations.CreateModel(
            name='ExecutiveDirector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('is_worked', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Наименование района')),
                ('executive_director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='executive_director', to='checks.executivedirector')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('significance_score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('isExists', models.BooleanField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='checks.location')),
            ],
        ),
        migrations.CreateModel(
            name='CorrectionReportComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('correction_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checks.correctionreport')),
            ],
        ),
        migrations.AddField(
            model_name='controlevent',
            name='object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checks.object', verbose_name='Объект'),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checks.controlevent')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checks.grade', verbose_name='Оценка')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='checks.question', verbose_name='Вопрос')),
            ],
            options={
                'unique_together': {('control_event', 'question', 'grade')},
            },
        ),
    ]
