from django.http import response
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from collections import OrderedDict
from employee import serializers
from config.configurations import *

from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from employee.models import Users
from employee.serializers import UserSerializer

class RenderHome(APIView):
    @csrf_exempt    
    def get(self, request):
        return render(request, 'home/home.html', config_dict)