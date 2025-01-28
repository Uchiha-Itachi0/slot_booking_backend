from rest_framework import status
from rest_framework.decorators import api_view

from slot_booking_backend.utils.response import create_response

from ..models import CustomUser
from ..serializers.jwt import generate_token_for_user
from ..serializers.otp_serializer import OTPRequestSerialize, OTPVerificationSerializer


@api_view(['POST'])
def request_otp(request):
    """
    View to request an OTP by providing a valid email
    """

    serializer = OTPRequestSerialize(data=request.data)

    if serializer.is_valid():
        data = serializer.save()
        return create_response(
            success=True, message='OTP sent to the provided email', data=data, status_code=status.HTTP_200_OK
        )
    return create_response(
        success=False, message='Failed to send OTP', errors=serializer.errors, status_code=status.HTTP_400_BAD_REQUEST
    )


@api_view(['POST'])
def verify_otp(request):
    """
    View to verify the OTP for the provided email
    """

    serializer = OTPVerificationSerializer(data=request.data)

    if serializer.is_valid():
        email = serializer.validated_data['email']

        # Check if the user exists
        user = CustomUser.objects.filter(email=email).first()

        if user:
            # User found, generate tokens
            tokens = generate_token_for_user(user)

            data = {
                'tokens': tokens,
                'new_user': False,
            }
            return create_response(
                success=True,
                message='Successfully logged in',
                data=data,
                status_code=status.HTTP_200_OK,
                new_user=False,
                user_type=user.user_type
            )
        else:
            # User not found, respond with 'new_user' flag
            data = {'new_user': True}
            return create_response(
                success=True,
                message='User does not exist. Redirect to registration',
                status_code=status.HTTP_200_OK,
                data=data
            )

    return create_response(
        success=False,
        message='Failed to verify the OTP',
        errors=serializer.errors,
        status_code=status.HTTP_400_BAD_REQUEST
    )
