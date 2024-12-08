from django.urls import path
from .views import BoardListCreateView, BoardDetailView, ColumnListCreateView, ColumnDetailView

urlpatterns = [
    path('boards/', BoardListCreateView.as_view(), name='board-list-create'),
    path('boards/<int:pk>/', BoardDetailView.as_view(), name='board-detail'),
    path('boards/<int:pk>/columns/', ColumnListCreateView.as_view(), name='column-list-create'),
    path('boards/<int:pk>/columns/<int:column_pk>/', ColumnDetailView.as_view(), name='column-detail'),
]

