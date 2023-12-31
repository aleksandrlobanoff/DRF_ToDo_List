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
        """
        Create a new task and associate it with the provided categories.
        """
        categories_data = validated_data.pop('categories')
        task = Task.objects.create(**validated_data)
        for category_data in categories_data:
            category = Category.objects.get(pk=category_data['id'])
            task.categories.add(category)
        return task

    def update(self, instance, validated_data):
        categories_data = validated_data.pop('categories', [])

        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.file = validated_data.get('file', instance.file)
        instance.save()

        instance.categories.clear()
        for category_data in categories_data:
            category_id = category_data.get('id')
            try:
                category = Category.objects.get(pk=category_id)
                instance.categories.add(category)
            except Category.DoesNotExist:
                continue

        return instance
