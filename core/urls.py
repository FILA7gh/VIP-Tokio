from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
# from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenObtainPairView

import core.settings.base
from core.settings.base import MEDIA_URL, MEDIA_ROOT
from .settings import swagger


urlpatterns = [
    path('admin/', admin.site.urls),

    # models
    path('api/v1/models/', include('apps.models.urls')),
    # others
    path('api/v1/others/', include('apps.others.urls')),
    # users
    path('api/v1/users/', include('apps.users.urls')),

]

urlpatterns += swagger.urlpatterns

if core.settings.base.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


