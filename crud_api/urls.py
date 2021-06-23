from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from .views import ItemView

app_name = 'crud_api'

urlpatterns = [
    path('', csrf_exempt(ItemView.as_view()), name='item views'),
    path('<int:pk>/', csrf_exempt(ItemView.as_view()), name='item views'),
]