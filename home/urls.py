from django.urls import path
from home.views import *

urlpatterns = [
    path('', RenderHome.as_view())
]