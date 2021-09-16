from django.urls import path
from dashboard.views import *

urlpatterns = [
    path('', renderDashboard.as_view()),
    path('new/', createArea.as_view()),
    path('delete/<int:id>/', DeleteUser.as_view()),
    path('update/<int:id>/', UpdateUser.as_view()),
]