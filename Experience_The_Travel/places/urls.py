from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search',views.search,name='search'),
    path('details/<int:pk>/',views.details,name='details'),
    path('filter',views.filter,name='filter')
]