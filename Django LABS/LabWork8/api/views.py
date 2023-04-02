from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *
from .models import *


def index(request):
    return HttpResponse("Hello Rasul")


@api_view(['GET'])
def getProdById(request, id):
    prod = product.objects.all()
    serializer = ProductSerializer(prod, many=True)
    return Response(serializer.data[id])


def getProductsByCategoryId(request):
    return HttpResponse("Get pr by category")


@api_view(['GET'])
def getCategById(request, id):
    cat = Category.objects.all()
    serializer = CategorySerializer(cat, many=True)
    return Response(serializer.data[id])


@api_view(['GET'])
def getAllProducts(request):
    prod = product.objects.all()
    serializer = ProductSerializer(prod, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getAllCategories(request):
    cat = Category.objects.all()
    serializer = CategorySerializer(cat, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def postProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def postCategory(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data)
