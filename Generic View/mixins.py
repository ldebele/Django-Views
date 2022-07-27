from rest_framework import mixins
from rest_framework.generics import GenericAPIView

from .models import Item
from .serializers import ItemSerializer


class ItemList(mixins.ListModelMixin, mixins.CreateModelMixin,
                GenericAPIView):
    
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ItemDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                 mixins.DestroyModelMixin, GenericAPIView):
    
    queryset = Item.object.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)