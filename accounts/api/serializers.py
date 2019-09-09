from rest_framework import serializers
from accounts.models import User
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email',)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect credentials detected by account backend in django")
