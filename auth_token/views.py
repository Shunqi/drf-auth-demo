from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class TestView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 
    
    def get(self, request):
        users = [str(user) for user in User.objects.all()]
        return JsonResponse({'users': users})