from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404


from .models import Item, Message

def index(request):
    items = Item.objects.all()
    messages = Message.objects.all()
    template = loader.get_template('crud_templated/index.html')
    context = {'items': items, 'messages':messages}
    return HttpResponse(template.render(context, request))

def item_detail(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return render(request, 'crud_templated/404.html', {'name': 'item'})
    return render(request, 'crud_templated/detail.html', {'item': item, 'type':'Item'})

def message_detail(request, pk):
    try:
        message = Message.objects.get(pk=pk)
    except Message.DoesNotExist:
        return render(request, 'crud_templated/404.html', {'name': 'item'})
    return render(request, 'crud_templated/detail.html', {'message': message, 'type':'Message'})