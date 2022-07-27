from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer

from .models import Item
from .serializers import ItemSerializer



class ItemList(APIView):
    
    def get(self, request):
        Item = Item.objects.all()
        serializer = ItemSerializer(Item, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ItemDetail(APIView):

    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        Item = self.get_object(pk)
        serializer = ItemSerializer(Item)
        return Response(serializer.data)

    def put(self, request, pk):
        Item = self.get_object(pk=pk)
        serializer = ItemSerializer(Item, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Item = self.get_object(pk=pk)
        Item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        

# If you want to override the default class-based view
class ItemNotDone(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def get(self, request):
        user_count = Item.objects.filter(done=False).count()
        content = {'Not Done users': user_count}
        return Response(content)

