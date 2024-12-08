from rest_framework import generics
from ..models import Board
from ..serializers import BoardSerializer

class BoardListCreateView(generics.ListCreateAPIView):
    queryset = Board.objects.all().order_by('created_at')
    serializer_class = BoardSerializer

class BoardDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
