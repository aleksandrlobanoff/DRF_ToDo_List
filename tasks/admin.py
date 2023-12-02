from django.contrib import admin

from tasks.models import Task, Category


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'file', 'categories', 'created_at')
    readonly_fields = ('created_at',)
    list_display = ('title', 'description', 'created_at', 'display_categories')
    list_filter = ('title', 'created_at', 'categories')

    def display_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])

    display_categories.short_description = 'Categories'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'description')
    list_display = ('name', 'description')
    list_filter = ('description',)
