from django.urls import path
from .import views

urlpatterns = [
    path('cafeApplication/', views.sayhello, name='sayhello')
]