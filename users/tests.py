from rest_framework.test import APITestCase
from .models import User
from django.urls.base import reverse


class UserAPITestCase(APITestCase):

    def setUp(self):
        self.user_current = User.objects.create_user(email="test_1@test.com", username="test_1", password="1234",
                                                     first_name="test_1", last_name="test_1")
        self.user_other = User.objects.create_user(email="test_2@test.com", username="test_2")

    def test_token_obtain_pair_and_refresh(self):
        url = reverse("users:token_obtain_pair")
        response = self.client.post(url, data={"email": self.user_current.email, "password": "1234"})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json().get("refresh"))
        self.assertTrue(response.json().get("access"))

        url = reverse("users:token_refresh")
        response = self.client.post(url, data={"refresh": response.json().get("refresh")})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json().get("access"))

    def test_user_retrieve(self):
        url = reverse("users:user_retrieve", kwargs={"pk": self.user_current.id})

        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)

        self.client.force_authenticate(self.user_other)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

        self.client.force_authenticate(self.user_current)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 7)
        self.assertEqual(response.json().get("id"), self.user_current.id)

    def test_user_create(self):
        url = reverse("users:user_create")
        user_data = {"email": "test@test.com", "username": "test", "password": "1234"}

        response = self.client.post(url, data=user_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.json()), 12)
        self.assertTrue(response.json().get("id"))
        self.assertEqual(response.json().get("is_active"), True)
        self.assertEqual(response.json().get("is_staff"), False)
        self.assertEqual(response.json().get("password"), None)

    def test_user_update_put(self):
        url = reverse("users:user_update", kwargs={"pk": self.user_current.id})
        user_data = {"email": "test@test.com", "username": "test"}

        response = self.client.put(url, data=user_data)
        self.assertEqual(response.status_code, 401)

        self.client.force_authenticate(self.user_other)
        response = self.client.put(url, data=user_data)
        self.assertEqual(response.status_code, 403)

        self.client.force_authenticate(self.user_current)
        response = self.client.put(url, data=user_data)
        self.assertEqual(response.json().get("email"), user_data.get("email"))
        self.assertEqual(response.json().get("username"), user_data.get("username"))

    def test_user_update_patch(self):
        url = reverse("users:user_update", kwargs={"pk": self.user_current.id})
        user_data = {"last_name": "test"}

        response = self.client.patch(url, data=user_data)
        self.assertEqual(response.status_code, 401)

        self.client.force_authenticate(self.user_other)
        response = self.client.patch(url, data=user_data)
        self.assertEqual(response.status_code, 403)

        self.client.force_authenticate(self.user_current)
        response = self.client.patch(url, data=user_data)
        self.assertEqual(response.json().get("last_name"), user_data.get("last_name"))
        self.assertEqual(len(response.json()), 7)

        response = self.client.patch(url, data={"is_staff": True})
        self.assertEqual(response.json().get("is_staff"), False)

        response = self.client.patch(url, data={"is_active": False})
        self.assertEqual(response.json().get("is_active"), True)

    def test_user_destroy(self):
        url = reverse("users:user_destroy", kwargs={"pk": self.user_current.id})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, 401)

        self.client.force_authenticate(self.user_other)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 403)

        self.client.force_authenticate(self.user_current)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
