from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('blog/details/<int:id>', views.details, name='details'),
    path('', views.index, name='index'),
]