from rest_framework.generics import ListAPIView
#from rest_framework import DjangoFilterBackend

from board.serializers import BoardSerializer
from board.models import Board

class BoardList(ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
#    filter_backends = (DjangoFilterBackend,)
#    filter_fields = ('id',)
