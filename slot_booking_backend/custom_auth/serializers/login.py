from django.contrib.auth import authenticate
from rest_framework import serializers

from .jwt import generate_token_for_user


class LoginSerializer(serializers.Serializer):
    """
    Serializer to handle user login (email and password)
    """

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        """
        Validate user's credentials
        """

        email = attrs['email']
        password = attrs['password']

        # Authenticate the user
        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError('Invalid credentials')

        attrs['user'] = user
        return attrs

    def create(self, validate_data):
        """
        Create token for successful authentication
        """

        user = validate_data['user']
        return generate_token_for_user(user)
