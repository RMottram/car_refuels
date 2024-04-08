from django.urls import path
from . import views

urlpatterns = [
    path('', views.refuels, name='refuels'),
    path('<int:refuel_id>/', views.delete_refuel, name='delete_refuel'),
]