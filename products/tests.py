from rest_framework.test import APITestCase
from .models import Product
from users.models import User
from django.urls.base import reverse


class ProductAPITestCase(APITestCase):

    def setUp(self):
        self.product_1 = Product.objects.create(name="product_1", type_model="model_1")
        self.product_2 = Product.objects.create(name="product_2", type_model="model_2")
        self.user_no_staff = User.objects.create_user(email="test1@test.com", username="user_1", is_staff=False)
        self.user_staff = User.objects.create_user(email="test2@test.com", username="user_2", is_staff=True)

    def test_product_list(self):
        url = reverse("products:product_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)

        self.client.force_authenticate(self.user_no_staff)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

        self.client.force_authenticate(self.user_staff)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.json()[0].get("id"), self.product_1.id)
        self.assertEqual(response.json()[1].get("id"), self.product_2.id)

    def test_product_retrieve(self):
        url = reverse("products:product_retrieve", kwargs={"pk": self.product_1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)

        self.client.force_authenticate(self.user_no_staff)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

        self.client.force_authenticate(self.user_staff)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 4)
        self.assertEqual(response.json().get("id"), self.product_1.id)
        self.assertEqual(response.json().get("name"), self.product_1.name)
        self.assertEqual(response.json().get("type_model"), self.product_1.type_model)
        self.assertEqual(response.json().get("launch_at"), self.product_1.launch_at)
