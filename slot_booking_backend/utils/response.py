from rest_framework import status
from rest_framework.response import Response


def create_response(success: bool, message: str, data=None, errors=None, status_code=status.HTTP_200_OK):
    """
    Generate a consistent JSON response.

    Args:
        success (bool): Indicates if the request was successful.
        message (str): Description of the response.
        data (dict, optional): Any additional data to include.
        errors (dict, optional): Validation or processing errors.
        status_code (int): HTTP status code.

    Returns:
        Response: DRF Response object.
    """
    return Response({
        'success': success,
        'message': message,
        'data': data or {},
        'errors': errors or {}
    },
                    status=status_code)  # noqa:  E126
