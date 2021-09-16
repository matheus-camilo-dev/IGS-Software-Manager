from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('employee/', include('employee.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
