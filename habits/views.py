from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitsPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitsSerializer


class HabitsViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Habit model
    """
    serializer_class = HabitsSerializer
    pagination_class = HabitsPaginator
    queryset = Habit.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        match self.action:
            case 'create' | 'update':
                queryset = queryset.filter(is_pleasant=True)
            case 'retrieve':
                queryset = queryset.filter(user=self.request.user)
            case 'list':
                queryset = queryset.filter(is_public=True)
        return queryset

    def get_permissions(self):
        if self.action in ('update', 'retrieve', 'destroy'):
            permission_classes = [IsOwner]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        self.object = serializer.save()
        self.object.user = self.request.user
        self.object.save()
