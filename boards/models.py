from django.db import models 

class Board(models.Model):
    name = models.CharField( max_length=100 )
    order = models.PositiveIntegerField( default=0 )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Column(models.Model):
    name = models.CharField( max_length=100 )
    board = models.ForeignKey(Board, related_name='columns', on_delete=models.CASCADE)
    order = models.PositiveIntegerField( default=0 )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    
class Task(models.Model):
    title = models.CharField( max_length=100 )
    description = models.TextField(blank=True, null=True)
    column = models.ForeignKey(Column, related_name='tasks', on_delete=models.CASCADE)
    order = models.PositiveIntegerField( default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class Subtask(models.Model):
    title = models.CharField( max_length=100 )
    is_completed = models.BooleanField(default=False)
    task = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE)
    order = models.PositiveIntegerField( default=0 )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
                            
    
