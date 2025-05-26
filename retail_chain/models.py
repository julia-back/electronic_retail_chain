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

    NODE_TYPE_CHOICES = {
        "factory": "Завод",
        "retail": "Розничная сеть",
        "entrepreneur": "Индивидуальный предприниматель",
    }

    name = models.CharField(max_length=255)
    contacts = models.ForeignKey(Contacts, unique=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    supplier = models.ForeignKey("self", blank=True, null=True, on_delete=models.SET_NULL)
    payment_arrears = models.DecimalField(max_digits=11, decimal_places=2)
    node_type = models.CharField(choices=NODE_TYPE_CHOICES)
    node_level = models.PositiveIntegerField(default=0, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.supplier:
            self.node_level = self.supplier.node_level + 1

        return super().save(*args, force_insert=force_insert, force_update=force_update,
                            using=using, update_fields=update_fields)

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"
        ordering = ["name"]
