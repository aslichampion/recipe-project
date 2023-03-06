from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('main.urls')),
    path('recipes/', include('recipes.urls')),
    path('admin/', admin.site.urls),
    path('members/', include('members.urls')),
    path('members/', include('django.contrib.auth.urls')),
]
