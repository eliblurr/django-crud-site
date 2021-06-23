from django.utils.decorators import method_decorator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.views import View
from .models import Item
import json

def simple_decorator(func):
    def inner(*args, **kwargs):
        print("Eli's personal decorator")
        return func(*args, **kwargs)
    return inner

class ItemView(View):
    LIMIT = 20
    SKIP = 0

    def get(self, request, pk=0, *args, **kwargs):
        if pk:
            item = get_object_or_404(Item, pk=pk)
            data = {
                'id':item.id,
                'title':item.title,
                'metatitle':item.metatitle,
                'description':item.description,
                'date_created':item.date_created,
                'date_modified':item.date_modified,
            }
            return JsonResponse(data, safe=False)
        items = Item.objects.all()[self.SKIP:self.SKIP+self.LIMIT]
        res = list(items.values())
        return JsonResponse(res, safe=False)
    
    @method_decorator(simple_decorator)
    def post(self, request, *args, **kwargs):
        payload = json.loads(request.body)
        item = Item(title=payload.get('title'), metatitle=payload.get('metatitle'), description=payload.get('description'))
        item.save()
        return HttpResponse(item.id,  content_type='application/json', status=201)

    def put(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        payload = json.loads(request.body)
        item.title = payload.get('title')
        item.metatitle = payload.get('metatitle')
        item.description = payload.get('description')
        item.save()
        data = {
            'id':item.id,
            'title':item.title,
            'metatitle':item.metatitle,
            'description':item.description,
            'date_created':item.date_created,
            'date_modified':item.date_modified,
        }
        return JsonResponse(data, safe=False, status=202)
    
    def patch(self, request, pk, *args, **kwargs):
        item = get_object_or_404(Item, pk=pk)
        payload = json.loads(request.body)
        Item.objects.filter(pk=pk).update(**payload)
        return JsonResponse(True, safe=False, status=202)

    def delete(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        item.delete()
        return HttpResponse(status=204)