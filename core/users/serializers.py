from .models import User
from rest_framework import serializers
from knox.models import AuthToken


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'address', 'zip_code', 'state', 'city']


class AuthTokenSerializer(serializers.Serializer):
    auth_token = serializers.SerializerMethodField()

    def get_auth_token(self, user):
        _, token = AuthToken.objects.create(user=user)
        return token
    

class UserRegisterSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = BaseUserSerializer.Meta.fields + ['password']

class UserRetrieveSerializer(AuthTokenSerializer, BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = BaseUserSerializer.Meta.fields + ['auth_token']

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)


class EmptySerializer(serializers.Serializer):
    pass
