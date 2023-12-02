from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.title}, {self.description}, {self.created_at}"

    class Meta:
        verbose_name = "task"
        verbose_name_plural = "tasks"