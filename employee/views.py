from django.http import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from collections import OrderedDict
from employee import serializers

from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from config.configurations import *
from employee.models import Users
from employee.serializers import UserSerializer

class UsersList(APIView):
    @csrf_exempt
    def get(self, request):
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True) 
        return JsonResponse({'status': 1, 'message': 'Successfully generated employee list!', 'data': serializer.data})

class Get_Delete_or_Update_User(APIView):
    def get_object(self, id):
        try:
            return Users.objects.get(pk=id)
        except Users.DoesNotExist:
            raise NotFound()

    @csrf_exempt
    def get(self, request, id):
        response = {"status": 0, "message": "Employee not found!"}
        users = Users.objects.filter(id=id)
        serializer = UserSerializer(users, many=True) 
        if len(serializer.data) > 0:
            data = dict(serializer.data[0])
            response = {"status": 1, "message": "Employee has been found!", "data": data}
        return JsonResponse(response)

    @csrf_exempt
    def put(self, request, id):
        users = self.get_object(id)
        serializer = UserSerializer(users, data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response({"status": 1, "message": "Employee has been updated successfully!", "data": serializer.data})
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def delete(self, request, id):
        users = self.get_object(id)
        users.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({'status': 1, 'message':"Employee has been deleted successfully!"})

class AddUser(APIView):
    @csrf_exempt
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status': 1, 'message': 'Employee has been added successfully!'})
        return JsonResponse(serializer.errors)
