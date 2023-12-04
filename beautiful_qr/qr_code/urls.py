from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="qr_create"),
    path("qr_code/<int:pk>/", views.qr_code_detail, name="qr_code_detail"),
    path("qr_code/<int:pk>/", views.qr_create, name="qr_create"),
]
