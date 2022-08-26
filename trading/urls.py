from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /trading/3/
    path('<int:trade_id>/', views.detail, name='detail'), 
    path('results/', views.results, name='results'),
    path('add/', views.add, name='add'),
]