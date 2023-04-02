from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.status import *
from .serializer import *
from .models import *


def index(request):
    return HttpResponse("Hello Rasul")


#  @api_view(['GET'])
#  def getProdById(request, id):
#      prod = product.objects.all()
#      serializer = ProductSerializer(prod, many=True)
#     return Response(serializer.data[id])

class ProductByIdView(APIView):
    def get(self, request, id):
        prod = Product.objects.filter(id=id).first()
        serializer = ProductSerializer(prod)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductsByCategoryView(APIView):
    def get(self, request, id):
        # Получаем продукты по категории
        products = Product.objects.filter(category__id=id)
        product_serializer = ProductSerializer(products, many=True)
        return Response(product_serializer.data, status=HTTP_200_OK)

    def post(self, request, id):
        category = Category.objects.filter(id=id).first()
        product = Product(
            name=request.data["name"],
            price=request.data["price"],
            description=request.data["description"],
            count=request.data["count"],
            is_active=request.data["is_active"]
        )
        product.save()
        category.products.add(product)
        return Response( status=HTTP_201_CREATED)


class CategoryByIdView(APIView):
    def get(self, request, id):
        cat = Category.objects.filter(id=id).first()
        serializer = CategorySerializer(cat)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductsView(APIView):
    def get(self, request):
        prod = Product.objects.all()
        serializer = ProductSerializer(prod, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data)


class CategoriesView(APIView):
    def get(self, request):
        cat = Category.objects.all()
        serializer = CategorySerializer(cat, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data)
