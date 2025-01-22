from rest_framework import status
from rest_framework.decorators import api_view

from slot_booking_backend.utils.response import create_response

from ..serializers.login import LoginSerializer


@api_view(['POST'])
def login_user(request):
    """
        Login an existing user (interviewer or interviewee).

        Args:
            request (Request): The HTTP request object containing user data in JSON format.

        Body Parameters:
            - email (str): Email address of the user.
            - password (str): Password for the account.

        Returns:
            Response: A JSON response containing a success message and tokens if successful.
                      Error details if the request is invalid.

        Responses:
            200 OK: User successfully logged in with tokens included.
            400 Bad Request: Invalid input data.
        """

    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        tokens = serializer.save()
        return create_response(success=True, message='Login successful', data=tokens, status_code=status.HTTP_200_OK)
    return create_response(
        success=False, message='Login failed', errors=serializer.errors, status_code=status.HTTP_400_BAD_REQUEST
    )
