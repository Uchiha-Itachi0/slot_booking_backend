from django.contrib import admin
from django.urls import include, path

urlpatterns = [path('admin/', admin.site.urls), path('auth/', include('slot_booking_backend.custom_auth.urls'))]
