from django.urls import path
from .views import LaptopList, LaptopDetail

urlpatterns = [
    path('', LaptopList.as_view(), name='laptop_list'),
    path('<int:pk>/', LaptopDetail.as_view(), name='laptop_detail'),
]