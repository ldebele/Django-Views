from django.db import models


class Item(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField()
    done = models.BooleanField()