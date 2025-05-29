from rest_framework.test import APITestCase
from users.models import User
from .models import ChainNode, Contacts
from products.models import Product
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
        self.user_no_staff = User.objects.create_user(email="test1@test.com", username="user_1", is_staff=False)
        self.user_staff = User.objects.create_user(email="test2@test.com", username="user_2", is_staff=True)

        self.contacts = Contacts.objects.create(email="test_1@test.com", country="country_1", city="city_1",
                                                street="street_1", house_number="house/1")
        self.product = Product.objects.create(name="product_1", type_model="model_1")
        self.chain_node_fabric = ChainNode.objects.create(name="chain_node_factory", contacts=self.contacts,
                                                          node_type="factory")
        self.chain_node_fabric.products.set([self.product.id])

    def test_chain_node_list(self):
        url = reverse("retail_chain:chain_node_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)

        self.client.force_authenticate(self.user_no_staff)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

        self.client.force_authenticate(self.user_staff)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0].get("id"), self.chain_node_fabric.id)

    def test_filter_by_contacts_country(self):
        contacts_2 = Contacts.objects.create(email="test_2@test.com", country="country_2", city="city_2",
                                             street="street_2", house_number="house/2")
        chain_node_fabric_2 = ChainNode.objects.create(name="chain_node_factory_2", contacts=contacts_2,
                                                       node_type="factory")

        contacts_3 = Contacts.objects.create(email="test_3@test.com", country="country_2", city="city_3",
                                             street="street_3", house_number="house/3")
        chain_node_fabric_3 = ChainNode.objects.create(name="chain_node_factory_3", contacts=contacts_3,
                                                       node_type="factory")

        url = reverse("retail_chain:chain_node_list")
        data_for_filter = {"contacts__country": "country_2"}

        self.client.force_authenticate(self.user_staff)

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)

        response = self.client.get(url, query_params=data_for_filter)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.json()[0].get("id"), chain_node_fabric_2.id)
        self.assertEqual(response.json()[1].get("id"), chain_node_fabric_3.id)

    def test_chain_node_retrieve(self):
        url = reverse("retail_chain:chain_node_retrieve", kwargs={"pk": self.chain_node_fabric.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)

        self.client.force_authenticate(self.user_no_staff)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

        self.client.force_authenticate(self.user_staff)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 9)
        self.assertEqual(response.json().get("id"), self.chain_node_fabric.id)
        self.assertEqual(response.json().get("name"), self.chain_node_fabric.name)
        self.assertEqual(response.json().get("contacts"), self.chain_node_fabric.contacts.id)
        self.assertEqual(response.json().get("products"),
                         [product.id for product in self.chain_node_fabric.products.all()])
        self.assertEqual(response.json().get("supplier"), self.chain_node_fabric.supplier)
        self.assertEqual(response.json().get("payment_arrears"), self.chain_node_fabric.payment_arrears)
        self.assertEqual(response.json().get("node_type"), self.chain_node_fabric.node_type)
        self.assertEqual(response.json().get("node_level"), self.chain_node_fabric.node_level)

    def test_chain_node_create(self):
        url = reverse("retail_chain:chain_node_create")
        contacts_2 = Contacts.objects.create(email="test_2@test.com", country="country_2", city="city_2",
                                             street="street_2", house_number="house/2")
        chain_node_data = {"name": "chain_node_fabric_2", "contacts": contacts_2.id, "node_type": "factory"}
        response = self.client.post(url, data=chain_node_data)
        self.assertEqual(response.status_code, 401)

        self.client.force_authenticate(self.user_no_staff)
        response = self.client.post(url, data=chain_node_data)
        self.assertEqual(response.status_code, 403)

        self.client.force_authenticate(self.user_staff)
        response = self.client.post(url, data=chain_node_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json().get("name"), chain_node_data.get("name"))
        self.assertEqual(response.json().get("contacts"), chain_node_data.get("contacts"))
        self.assertEqual(response.json().get("node_type"), chain_node_data.get("node_type"))

    def test_chain_node_update_put(self):
        url = reverse("retail_chain:chain_node_update", kwargs={"pk": self.chain_node_fabric.id})
        chain_node_data = {"name": "chain_node_fabric_3", "contacts": self.contacts.id, "node_type": "retail"}
        response = self.client.put(url, data=chain_node_data)
        self.assertEqual(response.status_code, 401)

        self.client.force_authenticate(self.user_no_staff)
        response = self.client.put(url, data=chain_node_data)
        self.assertEqual(response.status_code, 403)

        self.client.force_authenticate(self.user_staff)
        response = self.client.put(url, data=chain_node_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("name"), chain_node_data.get("name"))
        self.assertEqual(response.json().get("node_type"), chain_node_data.get("node_type"))

    def test_chain_node_update_patch(self):
        url = reverse("retail_chain:chain_node_update", kwargs={"pk": self.chain_node_fabric.id})
        chain_node_data = {"name": "chain_node_fabric_3"}
        response = self.client.patch(url, data=chain_node_data)
        self.assertEqual(response.status_code, 401)

        self.client.force_authenticate(self.user_no_staff)
        response = self.client.patch(url, data=chain_node_data)
        self.assertEqual(response.status_code, 403)

        self.client.force_authenticate(self.user_staff)
        response = self.client.patch(url, data=chain_node_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("name"), chain_node_data.get("name"))
        self.assertEqual(response.json().get("node_type"), self.chain_node_fabric.node_type)

    def test_chain_node_destroy(self):
        url = reverse("retail_chain:chain_node_destroy", kwargs={"pk": self.chain_node_fabric.id})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, 401)

        self.client.force_authenticate(self.user_no_staff)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 403)

        self.client.force_authenticate(self.user_staff)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_node_level_by_supplier(self):
        chain_node_2 = ChainNode.objects.create(name="retail_1", supplier=self.chain_node_fabric, node_type="retail")
        chain_node_3 = ChainNode.objects.create(name="entrepreneur_2", supplier=chain_node_2, node_type="entrepreneur")
        chain_node_4 = ChainNode.objects.create(name="retail_2", supplier=chain_node_2, node_type="retail")
        chain_node_5 = ChainNode.objects.create(name="entrepreneur_3", supplier=chain_node_4, node_type="entrepreneur")

        self.assertEqual(ChainNode.objects.get(id=self.chain_node_fabric.id).node_level, 0)
        self.assertEqual(ChainNode.objects.get(id=chain_node_2.id).node_level, 1)
        self.assertEqual(ChainNode.objects.get(id=chain_node_3.id).node_level, 2)
        self.assertEqual(ChainNode.objects.get(id=chain_node_4.id).node_level, 2)
        self.assertEqual(ChainNode.objects.get(id=chain_node_5.id).node_level, 3)
