import random
import string

from django.core.cache import cache

from slot_booking_backend.utils.const import OTP_EXPIRY_TIME


def generate_otp(email: str, length: int = 6) -> str:
    """
    Generate and store otp for the given email
    Args:
        length: Integer ( default value is set to 6 )
        email: Email for which OTP is being generated

    Returns: OTP (type: Integer)

    """

    otp = ''.join(random.choices(string.digits, k=length))
    cache.set(email, otp, timeout=OTP_EXPIRY_TIME)
    return otp


def verify_otp_for_email(email: str, otp: str) -> bool:
    """
    Verify the OTP for the given email.
    Args:
        email: type str, Email for which you are verifying the OTP
        otp: type str, which you are verifying

    Returns: bool

    """
    cached_otp = cache.get(email)
    if cached_otp is None:
        return False
    return cached_otp == otp
