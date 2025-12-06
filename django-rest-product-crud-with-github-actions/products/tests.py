from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product

class SimpleAPITest(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Test', description='Desc', price=10.0, stock=5
        )
        self.list_url = reverse('product-list')
        self.detail_url = reverse('product-detail', args=[self.product.id])

    def test_fetch_product(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test')

    def test_update_product(self):
        data = {'name': 'Updated', 'description': 'Desc', 'price': 10.0, 'stock': 5}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated')

    def test_delete_product(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)




        