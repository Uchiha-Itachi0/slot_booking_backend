# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ba*+g4%c!c0qsy3_4m4w0hepzek=n&ah!^u9fo83zi*80y63^l'

LOGGING['formatters']['colored'] = {  # type: ignore # noqa: F821
    '()': 'colorlog.ColoredFormatter',
    'format': '%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s',
}
LOGGING['loggers']['slot_booking_backend']['level'] = 'DEBUG'  # type: ignore # noqa: F821
LOGGING['handlers']['console']['level'] = 'DEBUG'  # type: ignore # noqa: F821
LOGGING['handlers']['console']['formatter'] = 'colored'  # type: ignore # noqa: F821
