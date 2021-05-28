from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include([
        path('users/', include('users.urls')),
        path('app/', include('app.urls')),
    ])),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)