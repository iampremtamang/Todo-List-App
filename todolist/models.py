from django.db import models


class List(models.Model):
    task_name = models.CharField(max_length = 100)
    completed = models.BooleanField(default = False)

    def __str__ (self):
        return self.task_name
