from rest_framework import serializers

from habits.models import Habit
from habits.validators import PleasantHabitValidator, RelatedHabitValidator, CompleteTimeValidator


class HabitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            PleasantHabitValidator(field_1='is_pleasant', field_2='related_habit', field_3='reward'),
            RelatedHabitValidator(field_1='reward', field_2='related_habit'),
            CompleteTimeValidator(field='duration')
        ]
