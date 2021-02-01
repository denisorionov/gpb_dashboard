from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from dashboard.views import main_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view)
]

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
