from django.urls import path
from . import views

app_name = 'crud_templated'

urlpatterns = [
    path('', views.index, name='items'),
    path('<int:pk>/items/', views.item_detail, name='item detail'),
    path('<int:pk>/messages/', views.message_detail, name='message detail'),
]