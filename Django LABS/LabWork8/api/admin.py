from django.contrib import admin
from .models import product
from .models import Category

# Register your models here.
admin.site.register(product)
admin.site.register(Category)
