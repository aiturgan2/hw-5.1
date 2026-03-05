from django.urls import path
from app.settings.views import (
    SettingsListAPIView,
    SettingsCreateAPIView,
    PublicSettingsAPIView,
)

urlpatterns = [
    path("settings", SettingsListAPIView.as_view(), name='settings-list'), 
    path("settings/<str:key>", SettingsListAPIView.as_view(), name='settings-detail'),
    path("public/settings", PublicSettingsAPIView.as_view(), name='public-settings-list'),
    path("public/settings/<str:key>", PublicSettingsAPIView.as_view(), name='public-settings-detail'),
    path("settings_create", SettingsCreateAPIView.as_view(), name='settings-create')
]
