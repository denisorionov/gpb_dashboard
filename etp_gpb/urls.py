from django.conf import settings
from django.contrib import admin
from django.urls import path

from dashboard.views import main_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view)
]

urlpatterns += ('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
