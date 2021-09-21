from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from collections import OrderedDict
from config.configurations import *

from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from employee.models import Users
from employee.serializers import UserSerializer

def get_object(id):
    try:
        return Users.objects.get(pk=id)
    except Users.DoesNotExist:
        # raise NotFound()
        return None
        # raise JsonResponse({'status': 0, 'message': 'Employee not found!'})

class renderDashboard(APIView):
    @csrf_exempt    
    def get(self, request):
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        dados = []
        for i in range(0, len(serializer.data)):
            dados.append(dict(serializer.data[i]))
        if dados == []:
            return render(request, 'dashboard/dashboard.html', {'data' : dados, **config_dict, 'msg' : "Não há registros! Adicione um novo para administrar!"})
        return render(request, 'dashboard/dashboard.html', {'data' : dados, **config_dict})

class createArea(APIView):
    @csrf_exempt
    def get(self, request):
        return render(request, 'dashboard/new.html', config_dict)
    
    @csrf_exempt
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/dashboard/')    
        return render(request, 'dashboard/new.html', config_dict)

class DeleteUser(APIView):
    @csrf_exempt
    def get(self, request, id):
        users = get_object(id)
        users.delete()
        return redirect('/dashboard/')

class UpdateUser(APIView):
    @csrf_exempt
    def get(self, request, id):
        users = get_object(id)
        if(users != None):
            serializer = UserSerializer(users)
            return render(request, 'dashboard/update.html', {'dados' : serializer.data, **config_dict})
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    @csrf_exempt
    def post(self, request, id):
        users = get_object(id)
        if(users != None):
            serializer = UserSerializer(users, data=request.data)
            if serializer.is_valid():
                serializer.save() 
                return redirect("/dashboard/")
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
