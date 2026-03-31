from django.db import models

# Create your models here.
class Visitor(models.Model):
    total_count = models.IntegerField(default=0)

    def __str__(self):
        return "방문자 카운트"