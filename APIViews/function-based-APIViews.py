from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status

from .models import Item
from .serializers import ItemSerializer


# if we use function based api_view, we'll need to user api_view decorator
api_view(['DELETE'])
def delete_all_items(request):
    item = Item.objects.all()
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


api_view(['GET', 'POST'])
def Item_list(request):
    """List all Item and Create an new Item"""

    if request.method == 'GET':
        Item = Item.objects.all()
        serializer = ItemSerializer(Item, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


api_view(['GET', 'PUT', 'DELETE'])
def Item_detail(request, pk):
    """Retrieve and delete an item"""

    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    
    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ItemSerializer(item, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# use policy decorators if you want to override the default setting of function-based views (FBV)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def items_Not_done(request):
    item_count = Item.objects.filter(done=False).count()
    message = {'Not done iteme': item_count}
    return Response(message)