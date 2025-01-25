from rest_framework import serializers

from slot_booking_backend.utils.const import OTP_LENGTH

from ..services.email_service import send_otp_email
from ..services.otp_service import generate_otp, verify_otp_for_email


class OTPRequestSerialize(serializers.Serializer):
    """
    Serializer for requesting OTP
    """

    email = serializers.EmailField(required=True)

    def create(self, validated_data):
        """
        Generate and send OTP to the provided email
        """

        email = validated_data['email']
        otp = generate_otp(email=email, length=OTP_LENGTH)
        send_otp_email(to_email=email, otp=otp)
        return {'email': email}


class OTPVerificationSerializer(serializers.Serializer):
    """
    Serializer for verifying the OTP
    """

    email = serializers.EmailField(required=True)
    otp = serializers.CharField(required=True, max_length=OTP_LENGTH)

    def validate(self, attrs):
        """
        Validate the OTP
        """

        email = attrs.get('email')
        otp = attrs.get('otp')

        if not verify_otp_for_email(email=email, otp=otp):
            raise serializers.ValidationError({'otp': 'Invalid or expired OTP'})
        return attrs
