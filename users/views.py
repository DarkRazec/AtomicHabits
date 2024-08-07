from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from users.models import User
from users.serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
        ViewSet for User models
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # permission_classes = []

    def get_permissions(self):
        if self.action in ('create',):
            permission_classes = []
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
