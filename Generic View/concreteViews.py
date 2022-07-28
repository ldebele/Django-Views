from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Item
from .serializers import ItemSerializer


'''They providing 9 classes:
    - CreateAPIView
    - ListAPIView
    - RetrieveAPIView
    - DestoryAPIView
    - UpdateAPIView
    - ListCreateAPIView
    - RetrieveUpdateAPIView
    - RetrieveDestroyAPIView
    - RetrieveUpdateDestroyAPIView'''


class ListCreateItem(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemNotDone(ListAPIView):
    permission_classes = [IsAdminUser]

    queryset = Item.objects.all().filter(done=False)
    serializer_class = ItemSerializer

