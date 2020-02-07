from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.articles, name='projects'),
    path('post/<id>/', views.post, name='posts')
]