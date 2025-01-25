from django.conf import settings
from django.core.mail import send_mail


def send_email(to_email, subject, body):
    """
    Sends an email via Mailgun.
    """
    send_mail(
        subject=subject,
        message=body,
        html_message=body,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[
            to_email,
        ],
        fail_silently=False
    )


def send_otp_email(to_email, otp):
    """
    Sends an OTP to the user email via Mailgun.
    """
    subject = 'Your OTP for Login/Registration'
    body = f"""
    <html>
        <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px; color: #333;">
            <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 20px;
            border-radius: 10px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);">
                <h2 style="color: #4CAF50;">OTP for Login/Registration</h2>
                <p style="font-size: 16px;">Hello,</p>
                <p style="font-size: 16px;">
                    Your OTP is <strong style="font-size: 24px; color: #FF5722;">
                    {otp}</strong>. It will expire in 5 minutes.
                </p>
                <p style="font-size: 16px;">Please do not share this OTP with anyone
                 to keep your account secure.</p>
                <p style="font-size: 14px; color: #888;">
                    If you did not request this OTP, please ignore this email.
                </p>
                <footer style="font-size: 12px; text-align: center; color: #aaa;">
                    <p>Thank you for using our service.</p>
                    <p>Best regards,<br>bookmyslot008</p>
                </footer>
            </div>
        </body>
    </html>
    """
    send_email(to_email, subject, body)
