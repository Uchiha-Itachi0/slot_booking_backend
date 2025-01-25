from django.urls import path

from .views.otp import request_otp, verify_otp

urlpatterns = [
    path('request_otp/', request_otp, name='request_otp'),
    path('verify_otp/', verify_otp, name='verify_otp'),
]
