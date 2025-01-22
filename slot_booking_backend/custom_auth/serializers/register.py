from rest_framework import serializers

from ..models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration. Handles validation and creation
    of CustomUser instances.
    """

    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'password', 'confirm_password', 'user_type', 'company']
        extra_kwargs = {
            'password': {
                'write_only': True
            },  # Ensures the password is not exposed in responses
            'company': {
                'required': False
            }  # Make 'company' optional if user_type is not 'interviewer'
        }

    def validate(self, attrs: dict) -> dict:
        """
        Validates input data before creating a user instance.
        Ensures password matches confirm_password.
        """
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'confirm_password': 'Passwords do not match'})

        if attrs.get('user_type') == 'interviewer' and not attrs.get('company'):
            raise serializers.ValidationError({'company': 'Company is required for interviewers'})

        return attrs

    def create(self, validated_data: dict) -> CustomUser:
        """
        Creates a CustomUser instance after removing confirm_password.
        """
        validated_data.pop('confirm_password')  # Remove confirm_password as it's not needed for the model
        user = CustomUser.objects.create_user(**validated_data)
        return user
