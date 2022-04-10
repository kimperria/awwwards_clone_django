from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.getData, name='get'),
    path('post/', views.postData, name='post'),
]