from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}
DAILY = 'ежедневно'
WEEKLY = 'еженедельно'
FREQUENCY = (
    (DAILY, 'ежедневно'),
    (WEEKLY, 'еженедельно'),
)


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='пользователь', **NULLABLE)
    place = models.CharField(max_length=100, verbose_name='место')
    time = models.TimeField(verbose_name='время')
    action = models.CharField(max_length=100, verbose_name='действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='приятная привычка')
    related_habit = models.ForeignKey('self', default=None, on_delete=models.SET_NULL, verbose_name='связанная привычка', **NULLABLE)
    frequency = models.CharField(choices=FREQUENCY, default=DAILY, verbose_name='периодичность')
    reward = models.CharField(max_length=100, verbose_name='вознаграждение', **NULLABLE)
    duration = models.TimeField(verbose_name='время на выполнение')
    is_public = models.BooleanField(default=True, verbose_name='опубликовано')

    def __str__(self):
        return f"Я буду {self.action} в {self.time} в {self.place}."

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
        ordering = ('place', 'action', 'time', 'user',)
