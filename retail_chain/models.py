from django.db import models
from products.models import Product


class Contacts(models.Model):

    email = models.EmailField(max_length=255)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.email}, {self.country}"

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"


class ChainNode(models.Model):

    name = models.CharField(max_length=255)
    contacts = models.ForeignKey(Contacts, unique=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    supplier = models.ForeignKey("self", blank=True, null=True, on_delete=models.SET_NULL)
    payment_arrears = models.DecimalField(max_digits=11, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"
        ordering = ["name"]
