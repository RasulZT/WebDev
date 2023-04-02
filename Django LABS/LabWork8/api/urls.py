from django.urls import path
from api import views

urlpatterns = [
    path('post', views.postProduct, name='productCreate'),
    path('', views.index, name='home'),
    path('products/', views.getAllProducts, name='products'),
    path('products/<int:id>/', views.getProdById, name='product'),
    path('categories/<int:id>/products/', views.getProductsByCategoryId, name='productsByCategory'),
    path('categories/', views.getAllCategories, name='categories'),
    path('categories/post', views.postCategory, name='categoriesCreate'),
    path('categories/<int:id>', views.getCategById, name='category'),


]
