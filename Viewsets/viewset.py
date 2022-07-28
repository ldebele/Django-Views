from django.shortcuts import get_object_or_404

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


from .models import Item
from .serializers import ItemSerializer


class ItemViewSet(ViewSet):
    # queryset = Item.objects.all()

    def list(self, request):
        queryset = Item.objects.all()
        serializer = ItemSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Item.objects.all()
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)



    # you can create custom action with the @action decorator.
    # The detail parameter should be set as True if the action is meant for single object
    # and set as False if the action is meant for all object
    # The request method is optional if it 'GET' cause 'GET' is allowed by default.
    @action(detail=False, method='[GET'])
    def item_not_done(self, request):
        count_item = Item.objects.filter(done=False).count()

        return Response(count_item)