from rest_framework.serializers import ValidationError


class FactoryNotHaveSupplierValidator:

    def __call__(self, fields_dict):
        fields_dict = dict(fields_dict)
        node_type = fields_dict.get("node_type")
        supplier = fields_dict.get("supplier")
        if node_type == "factory":
            if (hasattr(supplier, "exists") and supplier.exists()) or (isinstance(supplier, list) and supplier):
                raise ValidationError("Завод не может иметь поставщика.")


class FactoryNotHavePaymentArrearsValidator:

    def __call__(self, fields_dict):
        fields_dict = dict(fields_dict)
        node_type = fields_dict.get("node_type")
        payment_arrears = fields_dict.get("payment_arrears")
        if node_type == "factory":
            if payment_arrears != 0 and payment_arrears is not None:
                raise ValidationError("Завод не может иметь долг перед поставщиком.")
