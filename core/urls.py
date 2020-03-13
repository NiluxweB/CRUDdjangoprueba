from django.urls import path
from .views import index, listarpersona, agregarpersona

urlpatterns = [
    path('', index, name="index"),
]