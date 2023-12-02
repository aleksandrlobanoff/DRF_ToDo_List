from rest_framework import serializers
from .models import Task, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class TaskSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'created_at', 'file', 'categories']

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        task = Task.objects.create(**validated_data)
        for category_data in categories_data:
            category = Category.objects.get(pk=category_data['id'])
            task.categories.add(category)
        return task
