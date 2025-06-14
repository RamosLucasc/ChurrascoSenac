from django.urls import path
from .views import index, churrasco

urlpatterns = [
    path('', index, name='index'), # Página inicial
    path('churrasco', churrasco, name='churrasco')
]