from django.db import models
from products.models import Product
from django.core.exceptions import ValidationError


class Contacts(models.Model):
    """Класс модели контактов."""

    email = models.EmailField(max_length=255)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)

    def __str__(self):
        """Метод строкового отображения контактов."""

        return f"{self.email}, {self.country}"

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"


class ChainNode(models.Model):
    """
    Класс модели звена цепи по продаже электроники.
    Содержит связанные поля контактов, продуктов, поставщика.
    Уровень звена цепи проставляется автоматически на основе уровня поставщика.
    """

    NODE_TYPE_CHOICES = {
        "factory": "Завод",
        "retail": "Розничная сеть",
        "entrepreneur": "Индивидуальный предприниматель",
    }

    name = models.CharField(max_length=255)
    contacts = models.ForeignKey(Contacts, unique=True, blank=True, null=True, on_delete=models.SET_NULL)
    products = models.ManyToManyField(Product, blank=True)
    supplier = models.ForeignKey("self", blank=True, null=True, on_delete=models.SET_NULL)
    payment_arrears = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    node_type = models.CharField(choices=NODE_TYPE_CHOICES)
    node_level = models.PositiveIntegerField(default=0, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Метод строкового отображения звена цепи."""

        return f"{self.name} - {self.node_level}, {self.node_type}"

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        """
        Переопределенный метод сохранения объекта цвена цепи.
        Устанавливает уровень звена цепи на основе уровня поставщика.
        """

        if self.supplier:
            self.node_level = self.supplier.node_level + 1
        else:
            self.node_level = 0

        return super().save(*args, force_insert=force_insert, force_update=force_update,
                            using=using, update_fields=update_fields)

    def clean(self):
        """Метод валидации полей звена цепи."""

        if self.supplier:
            if self.supplier.id == self.id:
                raise ValidationError("Организация не может иметь себя в качестве поставщика.")

        if self.payment_arrears:
            if self.payment_arrears < 0:
                raise ValidationError("Долг не может быть отрицательным числом.")

        if self.node_type == "factory":
            if self.supplier:
                raise ValidationError("Завод не может иметь поставщика.")
            if self.payment_arrears != 0 and self.payment_arrears is not None:
                raise ValidationError("Завод не может иметь задолженность перед поставщиком.")

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"
        ordering = ["name"]
