from rest_framework import status
from rest_framework.decorators import api_view

from slot_booking_backend.utils.response import create_response

from ..serializers.jwt import generate_token_for_user
from ..serializers.register import RegisterSerializer


@api_view(['POST'])
def register_user(request):
    """
        Register a new user (interviewer or interviewee).

        Args:
            request (Request): The HTTP request object containing user data in JSON format.

        Body Parameters:
            - name (str): Name of the user.
            - email (str): Email address of the user.
            - password (str): Password for the account.
            - confirm_password (str): Confirmation of the password.
            - user_type (str): Type of the user ('interviewer' or 'interviewee').
            - company (str, optional): Company name (required if user_type is 'interviewer').

        Returns:
            Response: A JSON response containing a success message and tokens if successful.
                      Error details if the request is invalid.

        Responses:
            201 Created: User successfully registered with tokens included.
            400 Bad Request: Invalid input data.
        """

    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        tokens = generate_token_for_user(user)
        return create_response(
            success=True,
            message='Successfully created a user with the given credential',
            data=tokens,
            status_code=status.HTTP_201_CREATED
        )
    return create_response(
        success=False,
        message='Validation error occurs',
        errors=serializer.errors,
        status_code=status.HTTP_400_BAD_REQUEST
    )
