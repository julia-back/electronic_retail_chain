from rest_framework.test import APITestCase
from users.models import User
from .models import ChainNode, Contacts
from django.urls.base import reverse


class ContactsAPITestCase(APITestCase):

    def setUp(self):
        self.user_no_staff = User.objects.create_user(email="test1@test.com", username="user_1", is_staff=False)
        self.user_staff = User.objects.create_user(email="test2@test.com", username="user_2", is_staff=True)

        self.contacts_1 = Contacts.objects.create(email="test_1@test.com", country="country_1", city="city_1",
                                                  street="street_1", house_number="house/1")
        self.contacts_2 = Contacts.objects.create(email="test_2@test.com", country="country_2", city="city_2",
                                                  street="street_2", house_number="house/2")

    def test_contacts_list(self):
        url = reverse("retail_chain:contacts_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)

        self.client.force_authenticate(self.user_no_staff)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

        self.client.force_authenticate(self.user_staff)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.json()[0].get("id"), self.contacts_1.id)
        self.assertEqual(response.json()[1].get("id"), self.contacts_2.id)

    def test_contacts_retrieve(self):
        url = reverse("retail_chain:contacts_retrieve", kwargs={"pk": self.contacts_1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)

        self.client.force_authenticate(self.user_no_staff)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

        self.client.force_authenticate(self.user_staff)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 6)
        self.assertEqual(response.json().get("id"), self.contacts_1.id)
        self.assertEqual(response.json().get("email"), self.contacts_1.email)
        self.assertEqual(response.json().get("country"), self.contacts_1.country)
        self.assertEqual(response.json().get("city"), self.contacts_1.city)
        self.assertEqual(response.json().get("street"), self.contacts_1.street)
        self.assertEqual(response.json().get("house_number"), self.contacts_1.house_number)

    def test_contacts_create(self):
        url = reverse("retail_chain:contacts_create")
        contacts_data = {"email": "test_3@test.com",
                         "country": "country_3",
                         "city": "city_3",
                         "street": "street_3",
                         "house_number": "house/3"}
        response = self.client.post(url, data=contacts_data)
        self.assertEqual(response.status_code, 401)

        self.client.force_authenticate(self.user_no_staff)
        response = self.client.post(url, data=contacts_data)
        self.assertEqual(response.status_code, 403)

        self.client.force_authenticate(self.user_staff)
        response = self.client.post(url, data=contacts_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json().get("email"), contacts_data.get("email"))
        self.assertEqual(response.json().get("country"), contacts_data.get("country"))
        self.assertEqual(response.json().get("city"), contacts_data.get("city"))
        self.assertEqual(response.json().get("street"), contacts_data.get("street"))
        self.assertEqual(response.json().get("house_number"), contacts_data.get("house_number"))

    def test_contacts_update_put(self):
        url = reverse("retail_chain:contacts_update", kwargs={"pk": self.contacts_1.id})
        contacts_data = {"email": "test_3@test.com",
                         "country": "country_3",
                         "city": "city_3",
                         "street": "street_3",
                         "house_number": "house/3"}
        response = self.client.put(url, data=contacts_data)
        self.assertEqual(response.status_code, 401)

        self.client.force_authenticate(self.user_no_staff)
        response = self.client.put(url, data=contacts_data)
        self.assertEqual(response.status_code, 403)

        self.client.force_authenticate(self.user_staff)
        response = self.client.put(url, data=contacts_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("email"), contacts_data.get("email"))
        self.assertEqual(response.json().get("country"), contacts_data.get("country"))
        self.assertEqual(response.json().get("city"), contacts_data.get("city"))
        self.assertEqual(response.json().get("street"), contacts_data.get("street"))
        self.assertEqual(response.json().get("house_number"), contacts_data.get("house_number"))

    def test_contacts_update_patch(self):
        url = reverse("retail_chain:contacts_update", kwargs={"pk": self.contacts_1.id})
        contacts_data = {"email": "test_3@test.com"}
        response = self.client.patch(url, data=contacts_data)
        self.assertEqual(response.status_code, 401)

        self.client.force_authenticate(self.user_no_staff)
        response = self.client.patch(url, data=contacts_data)
        self.assertEqual(response.status_code, 403)

        self.client.force_authenticate(self.user_staff)
        response = self.client.patch(url, data=contacts_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("email"), contacts_data.get("email"))
        self.assertEqual(response.json().get("country"), self.contacts_1.country)
        self.assertEqual(response.json().get("city"), self.contacts_1.city)
        self.assertEqual(response.json().get("street"), self.contacts_1.street)
        self.assertEqual(response.json().get("house_number"), self.contacts_1.house_number)

    def test_contacts_destroy(self):
        url = reverse("retail_chain:contacts_destroy", kwargs={"pk": self.contacts_1.id})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, 401)

        self.client.force_authenticate(self.user_no_staff)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 403)

        self.client.force_authenticate(self.user_staff)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)


class ChainNodeAPITestCase(APITestCase):

    def setUp(self):
        pass

    def test_chain_node_list(self):
        pass

    def test_filter_by_contacts_country(self):
        pass

    def test_chain_node_retrieve(self):
        pass

    def test_chain_node_create(self):
        pass

    def test_chain_node_update_put(self):
        pass

    def test_chain_node_update_patch(self):
        pass

    def test_chain_node_destroy(self):
        pass

    def test_factory_not_have_supplier(self):
        pass

    def test_factory_not_have_payment_arrears(self):
        pass

    def test_read_only_node_level_and_payment_arrears(self):
        pass

    def test_node_level_by_supplier(self):
        pass

    def test_supplier_not_self_supplier(self):
        pass

    def test_payment_arrears_not_negative(self):
        pass
