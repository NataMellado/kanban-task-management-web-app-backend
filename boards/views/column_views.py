from rest_framework import generics, status
from rest_framework.response import Response
from django.db import transaction
from django.shortcuts import get_object_or_404
from ..models import Column, Board
from ..serializers import ColumnSerializer

class ColumnListCreateView(generics.ListCreateAPIView):
    serializer_class = ColumnSerializer

    def get_queryset(self):
        board_id = self.kwargs.get('pk')
        return Column.objects.filter(board_id=board_id)

    def create(self, request, *args, **kwargs):	
        board_id = self.kwargs.get('pk')
        board = get_object_or_404(Board, pk=board_id)

        data = request.data
        if not isinstance(data, (list, dict)):
            return Response({"error": "Invalid data format"}, status=status.HTTP_400_BAD_REQUEST)

        many = isinstance(data, list)
        with transaction.atomic():
            serializer = self.get_serializer(data=data, many=many, context={'board': board})
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ColumnDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
