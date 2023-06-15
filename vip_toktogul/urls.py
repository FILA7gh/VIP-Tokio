from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from vip_toktogul.settings import MEDIA_URL, MEDIA_ROOT
from . import swagger


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/models/', include('apps.models.urls')),

    path('api/v1/users/', include('apps.users.urls'))

]

urlpatterns += swagger.urlpatterns
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
