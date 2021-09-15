from django.db import models
from datetime import date

# Create your models here.


class Users(models.Model):
    """ Модель пользователя, имеет только одно поле - 'id' """

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return str(self.id)


class Survey(models.Model):
    """Модель опроса"""

    title = models.CharField(
        max_length=255, verbose_name='Наименоваение опроса')
    
    start_date = models.DateField(
        auto_created=True, default=date.today, verbose_name="Начало опроса", editable=True)
   
    end_date = models.DateField(verbose_name='Будет окончен')
    
    description = models.TextField(blank=True, verbose_name='Описание')
    
    is_active = models.BooleanField(default=False, verbose_name='Активен')

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self) -> str:
        return self.title


class Question(models.Model):
    """ Модель вопроса """

    QUESTION_TYPES = [
        ('TEXT', 'Ответ текстом'),
        ('SELECT', 'Ответ с выбором одного варианта'),
        ('SELECT_MULTIPLE', 'Ответ с выбором нескольких вариантов')
    ]

    survey = models.ForeignKey(
        Survey, on_delete=models.CASCADE, verbose_name='Опрос')
    
    text = models.TextField(verbose_name='Текст вопроса')
    
    question_type = models.CharField(
        choices=QUESTION_TYPES, max_length=255, verbose_name='Тип вопроса')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self) -> str:
        return self.text


class Answer(models.Model):
    """ Модель ответа """

    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    
    data = models.TextField(verbose_name='Содержание ответа')
    
    user_id = models.ForeignKey(
        Users, default=1, on_delete=models.CASCADE, verbose_name='ID пользователя', blank=False)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self) -> str:
        return f'Ответ на вопрос: {self.question}'
