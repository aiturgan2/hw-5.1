from django.urls import path
from app.settings.views import (
    SettingsListAPIView,
    SettingsCreateAPIView,
    PublicSettingsAPIView,
)
"""Public API behaviour:

GET /api/v1/public/settings/           – only objects with ``is_public=True``,
                                          sorted by ``key``.
GET /api/v1/public/settings/<key>/     – return single setting by key;
                                          404 if it does not exist or is
                                          not public.

Non‑public endpoints (/settings/) are backed by a separate view and are not
restricted by ``is_public``.
"""
urlpatterns = [
    path("settings", SettingsListAPIView.as_view(), name='settings-list'), 
    path("settings/<str:key>", SettingsListAPIView.as_view(), name='settings-detail'),
    # public-facing endpoints (only ``is_public=True``)
    path("public/settings", PublicSettingsAPIView.as_view(), name='public-settings-list'),
    path("public/settings/<str:key>", PublicSettingsAPIView.as_view(), name='public-settings-detail'),
    path("settings_create", SettingsCreateAPIView.as_view(), name='settings-create')
]
