from . import views
from django.urls import path

urlpatterns = [
    path('', views.ListModelsView.as_view(), name='app')
]
