from django.contrib import admin
from django.urls import include, path
from roots.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('roots/', include('roots.urls', namespace='roots')),
    path('items/', include('items.urls', namespace='items')),
]
