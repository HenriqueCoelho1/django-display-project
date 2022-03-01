from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    is_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title}"
