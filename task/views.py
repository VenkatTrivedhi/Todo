from django.shortcuts import render
from .serializer import TaskSerializer,UserSerializer
from .models import Task,User
from rest_framework import generics,viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny


class UserApi(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes  =   [TokenAuthentication]
    permission_classes = [AllowAny]



class Create(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



class Change(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


