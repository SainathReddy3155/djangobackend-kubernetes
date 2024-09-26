from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# from .serializer import RegisterSerializer
# from .models import Register
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import generics
from .serializer import UserSerializer,AddProductSerializer,GetProductSerializer,DeleteProductSerializer
from .models import AddProduct

def home(request):
    return HttpResponse("HELLOO")


class CreateUserView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[AllowAny]

class AddProductView(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=AddProductSerializer
    queryset=AddProduct.objects.all()

    def post(self,request):
        serializer=AddProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.error,status=400)


class GetProductAPIView(generics.ListAPIView):
    queryset=AddProduct.objects.all()
    permission_classes=[AllowAny]
    serializer_class=GetProductSerializer

class DeleteProductAPIView(generics.DestroyAPIView):
    queryset=AddProduct.objects.all()
    permission_classes=[AllowAny]
    serializer_class=DeleteProductSerializer
    lookup_field='product_id'

    