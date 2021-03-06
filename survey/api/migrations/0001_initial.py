# Generated by Django 2.2.10 on 2021-09-15 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименоваение опроса')),
                ('start_date', models.DateField(auto_now_add=True, verbose_name='Начало опроса')),
                ('end_date', models.DateField(verbose_name='Будет окончен')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активен')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст вопроса')),
                ('question_type', models.CharField(choices=[('TEXT', 'Ответ текстом'), ('SELECT', 'Ответ с выбором одного варианта'), ('SELECT_MULTIPLE', 'Ответ с выбором нескольких вариантов')], max_length=255, verbose_name='Тип вопроса')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Survey', verbose_name='Опрос')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField(verbose_name='Содержание ответа')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Question', verbose_name='Вопрос')),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Users', verbose_name='ID пользователя')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]
