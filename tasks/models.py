from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='task_files/', null=True, blank=True)
    categories = models.ManyToManyField('Category', related_name='tasks', blank=True)

    def __str__(self):
        return f"{self.title}, {self.description}, {self.created_at}"

    class Meta:
        verbose_name = "task"
        verbose_name_plural = "tasks"
