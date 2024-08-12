from celery import shared_task
from habits.models import Habit

from datetime import datetime
from habits.services import send_tg_message


@shared_task
def send_habit() -> None:
    """
    Sending habit's data to user's telegram with send_tg_message function
    """
    current_time = datetime.now().time()
    habits = Habit.objects.filter(time__lte=current_time)
    [send_tg_message(habit.user.tg_chat_id, habit) for habit in habits]

