from datetime import time

from rest_framework import serializers


class PleasantHabitValidator:

    def __init__(self, field_1, field_2, field_3):
        self.field_1 = field_1
        self.field_2 = field_2
        self.field_3 = field_3

    def __call__(self, habit):
        if habit.get(self.field_1) and (habit.get(self.field_2) or habit.get(self.field_3)):
            raise serializers.ValidationError(
                "A pleasant habit shouldn't have a related habit or reward")


class RelatedHabitValidator:

    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, habit):
        if habit.get(self.field_1) and habit.get(self.field_2):
            raise serializers.ValidationError(
                "A habit shouldn't have both 'reward' and 'related_habit' at the same time")


class CompleteTimeValidator:

    def __init__(self, field):
        self.field = field
        self.time = time(minute=2)

    def __call__(self, habit):
        if habit.get(self.field) > self.time:
            raise serializers.ValidationError(
                "Value 'duration' should be <= 2 min")
