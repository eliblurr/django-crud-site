from django.views.decorators.csrf import csrf_exempt
from django.urls import path, register_converter
from . import converters, views

# register_converter(converters.FourDigitYearConverter, 'yyyy')
app_name = 'crud_restful_api'

urlpatterns = [
    path('', views.index, name='index'),
    path('items/', views.ItemView.as_view(), name='ItemView'),
    path('items/<int:pk>/', views.ItemView.as_view(), name='ItemViewPK'),
    path('messages/', views.MessageView.as_view(), name='MessageView'),
    path('messages/<int:pk>/', views.MessageView.as_view(), name='MessageViewPK'),
    # path('<yyyy:year>/', <>, name='custom year'),
]