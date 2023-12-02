from django.contrib import admin

from tasks.models import Task, Category


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Task model.
    """
    fields = ('title', 'description', 'file', 'categories', 'created_at')
    readonly_fields = ('created_at',)
    list_display = ('title', 'description', 'created_at', 'display_categories')
    list_filter = ('title', 'created_at', 'categories')

    def display_categories(self, obj):
        """
        Display the categories associated with the task.
        """
        return ", ".join([category.name for category in obj.categories.all()])

    display_categories.short_description = 'Categories'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Category model.
    """
    fields = ('name', 'description')
    list_display = ('name', 'id', 'description')
    list_filter = ('description',)
