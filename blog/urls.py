from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:Blog_id>/', views.info, name='info')
]
