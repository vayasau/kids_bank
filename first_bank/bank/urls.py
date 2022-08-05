from django.urls import path
from . import views


urlpatterns = [
    path('', views.start, name='start'),
    path('<str:user_id>/', views.money, name='money'),
]