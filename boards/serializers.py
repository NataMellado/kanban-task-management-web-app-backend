from rest_framework import serializers
from .models import Board, Column, Task, Subtask

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = '__all__'
        
class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True, read_only=True)
    
    class Meta:
        model = Task
        fields = '__all__'


class ColumnSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    
    class Meta:
        model = Column
        fields = ['id', 'name', 'order', 'tasks', 'created_at', 'updated_at', 'board']
        read_only_fields = ['board']
    
    def create(self, validated_data):
        board = self.context['board']
        return Column.objects.create(board=board, **validated_data)
        
class BoardSerializer(serializers.ModelSerializer):
    columns = ColumnSerializer(many=True, read_only=True)
    
    class Meta:
        model = Board
        fields = '__all__'