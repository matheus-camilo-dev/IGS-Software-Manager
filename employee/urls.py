from django.urls import path
from employee.views import UsersList, AddUser, Get_Delete_or_Update_User

urlpatterns = [
    path('', UsersList.as_view()),
    path('<int:id>', Get_Delete_or_Update_User.as_view()),
    path('add/', AddUser.as_view()),
]