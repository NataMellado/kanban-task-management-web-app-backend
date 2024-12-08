# Generated by Django 5.1 on 2024-12-08 15:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_remove_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='name',
            field=models.CharField(error_messages={'blank': 'El nombre no puede estar vacío.', 'unique': 'Ya existe un elemento con ese nombre.'}, max_length=100, unique=True, validators=[django.core.validators.MaxLengthValidator(100, message='El nombre no puede exceder 100 caracteres.')]),
        ),
        migrations.AlterField(
            model_name='board',
            name='order',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0, message='El orden debe ser un número mayor o igual a 0.')]),
        ),
        migrations.AlterField(
            model_name='column',
            name='name',
            field=models.CharField(error_messages={'blank': 'El nombre no puede estar vacío.', 'unique': 'Ya existe un elemento con ese nombre.'}, max_length=100, unique=True, validators=[django.core.validators.MaxLengthValidator(100, message='El nombre no puede exceder 100 caracteres.')]),
        ),
        migrations.AlterField(
            model_name='column',
            name='order',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0, message='El orden debe ser un número mayor o igual a 0.')]),
        ),
        migrations.AlterField(
            model_name='subtask',
            name='order',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0, message='El orden debe ser un número mayor o igual a 0.')]),
        ),
        migrations.AlterField(
            model_name='subtask',
            name='title',
            field=models.CharField(error_messages={'blank': 'El nombre no puede estar vacío.'}, max_length=100, validators=[django.core.validators.MaxLengthValidator(100, message='El nombre no puede exceder 100 caracteres.')]),
        ),
        migrations.AlterField(
            model_name='task',
            name='order',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0, message='El orden debe ser un número mayor o igual a 0.')]),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(error_messages={'blank': 'El nombre no puede estar vacío.'}, max_length=100, validators=[django.core.validators.MaxLengthValidator(100, message='El nombre no puede exceder 100 caracteres.')]),
        ),
    ]