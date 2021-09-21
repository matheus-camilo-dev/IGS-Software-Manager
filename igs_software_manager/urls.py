from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from . import settings

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('employee/', include('employee.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('api-auth/', include('rest_framework.urls')), 
]
