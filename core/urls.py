from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from core.settings.base import MEDIA_URL, MEDIA_ROOT
from .settings import swagger


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/models/', include('apps.models.urls')),

    path('api/v1/others/', include('apps.others.urls')),

    path('api/v1/users/', include('apps.users.urls')),

    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

]

urlpatterns += swagger.urlpatterns
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
