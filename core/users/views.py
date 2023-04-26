from django.contrib.auth import logout
from .models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from base.serializers import MultipleSerializerMixin
from .serializers import *


class UserAuthenticationViewSet(MultipleSerializerMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny,]
    serializer_class = EmptySerializer
    response_serializer_class = UserRetrieveSerializer
    serializer_classes = {
        'login': UserLoginSerializer,
        'register': UserRegisterSerializer
    }

    @action(detail=False, methods=['POST'], url_path='login')
    def login(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_and_authenticate_user(**serializer.validated_data)
        response_data = self.response_serializer_class(user,  context=self.get_serializer_context()).data
        return Response(data=response_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'], url_path='register')
    def register(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create(**serializer.validated_data)
        response_data = self.response_serializer_class(user, context=self.get_serializer_context()).data
        return Response(data=response_data, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['POST'], permission_classes=[IsAuthenticated])
    def logout(self, request, *args, **kwargs):
        logout(request)
        data = {"success": "Successfully logged out"}
        return Response(data=data, status=status.HTTP_200_OK)
