from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('product/<int:product_id>/', change_product, name='product'),
    path('category/<int:cat_id>/', show_category, name='category'),
]
