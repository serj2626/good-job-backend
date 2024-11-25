from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("api/", include("core.urls")),
    path("api/auth/", include("accounts.urls")),
    path("api/contacts/", include("contacts.urls")),
    path("api/chats/", include("chats.urls")),
    path("api/notifications/", include("notifications.urls")),
    path("api/employees/", include("employees.urls")),
    path("api/companies/", include("companies.urls")),
    path("api/favorites/", include("favorites.urls")),
]


if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
