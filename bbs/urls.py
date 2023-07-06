from django.urls import path
from . import views
from .models import Article
from django.views import generic

app_name = 'bbs'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:id>/', views.detail, name='detail'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create/', views.create, name='create'),
    # path('<int:id>/update', views.update, name='update'),
    path('<int:pk>/update/', views.UpdateView.as_view(), name='update'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('create/', views.CreateView.as_view(), name='create'),
]
