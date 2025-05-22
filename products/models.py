from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=255)
    type_model = models.CharField(max_length=255)
    launch_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
