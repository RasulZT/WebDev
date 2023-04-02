from django.urls import path
from api.views import *

urlpatterns = [
    path('', index, name='home'),
    path('products/', ProductsView.as_view(), name='products'),
    path('products/<int:id>/', ProductByIdView.as_view(), name='product'),
    path('categories/<int:id>/products/', getProductsByCategoryId, name='productsByCategory'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('categories/<int:id>', CategoryByIdView.as_view(), name='category'),
]
