from django.http import response
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from collections import OrderedDict
from employee import serializers

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
        raise NotFound()

class renderDashboard(APIView):
    @csrf_exempt    
    def get(self, request):
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        dados = []
        for i in range(0, len(serializer.data)):
            dados.append(dict(serializer.data[i]))
        return render(request, 'dashboard/dashboard.html', {"data" : dados})

class createArea(APIView):
    @csrf_exempt
    def get(self, request):
        return render(request, 'dashboard/new.html')
    
    @csrf_exempt
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/dashboard/')    
        return render(request, 'dashboard/new.html')

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
        serializer = UserSerializer(users)
        return render(request, 'dashboard/update.html', {'dados' : serializer.data})

    @csrf_exempt
    def post(self, request, id):
        users = get_object(id)
        serializer = UserSerializer(users, data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return redirect("/dashboard/")
        return HttpResponse("Ocorreu um problema: "+str(serializer.erros))
