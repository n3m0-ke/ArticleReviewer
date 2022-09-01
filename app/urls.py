from django.urls import path
from . import views

urlpatterns = [
    path('revisor/', views.index, name='index'),
    path('rewrite/', views.rewrite, name='rewrite'),
    path('preview/', views.preview, name='preview'),
]