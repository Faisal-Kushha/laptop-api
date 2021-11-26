from django.db import models
from django.contrib.auth import get_user_model


class Laptop(models.Model):
    brand = models.CharField(max_length=64)
    description = models.TextField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add = True, null=True)
    updated_at = models.DateTimeField(auto_now = True, null=True)

    def __str__(self):
        return self.brand