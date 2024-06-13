from django.urls import path
from .views import chart,create


urlpatterns = [
    path('',create,name='create'),
    path('chart_view/',chart,name='chart_view')
]