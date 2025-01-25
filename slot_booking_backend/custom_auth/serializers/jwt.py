from typing import Dict

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class TokenSerializer(serializers.Serializer):
    """
    Serializer for JWT tokens.

    Serializes the refresh token and access token fields.
    """
    refresh_token = serializers.CharField(help_text='Refresh token for renewing access tokens.')
    access_token = serializers.CharField(help_text='Access token for authenticating API requests.')


def generate_token_for_user(user) -> Dict[str, str]:
    """
    Generate JWT tokens (refresh and access) for the given user.

    Args:
        user (User): The user instance for whom the tokens are being generated.

    Returns:
        Dict[str, str]: A dictionary containing the refresh and access tokens.
    """
    refresh_token = RefreshToken.for_user(user)
    access_token = refresh_token.access_token

    # Add user_type to the token's payload
    access_token['user_type'] = user.user_type
    return {'refresh_token': str(refresh_token), 'access_token': str(access_token)}
