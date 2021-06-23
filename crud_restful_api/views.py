from .models import Message, Item
from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from  .serializers import MessageSerializer, ItemSerializer

def index(request):
    return HttpResponse('django simple api with restful', status=200)

class ItemView(APIView):
    serializer = ItemSerializer
    model = Item

    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def get(self, request, pk=0, skip=0, limit=100):
        if pk:
            data = self.serializer(self.get_object(pk)).data
        else:   
            item = Item.objects.all()[skip:skip+limit]
            data = self.serializer(item, many=True).data
        return Response(data)

    def post(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        serializer = self.serializer(self.get_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        serializer = self.serializer(self.get_object(pk), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        item = self.get_object(pk)
        item.delete()
        return Response(status=204)

class MessageView(APIView):
    serializer = MessageSerializer
    model = Message

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def get(self, request, pk=0, skip=0, limit=100):
        if pk:
            data = self.serializer(self.get_object(pk)).data
        else:   
            message = self.model.objects.all()[skip:skip+limit]
            data = self.serializer(message, many=True).data
        return Response(data)

    def post(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        serializer = self.serializer(self.get_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        serializer = self.serializer(self.get_object(pk), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        message = self.get_object(pk)
        message.delete()
        return Response(status=204)