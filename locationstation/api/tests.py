from django.test import TestCase
from rest_framework.test import APIClient
from .models import Listing

class TestApiView(TestCase):
    def setUp(self):
        self.client = APIClient()
        Listing.objects.create(
            neighbourhood_group="Manchester",
            neighbourhood='Ardwick',
            latitude=53.4401,
            longitude=-2.28187,
            price=33
        )
        Listing.objects.create(
            neighbourhood_group="Manchester",
            neighbourhood='Hulme',
            latitude=53.4394,
            longitude=2.28205,
            price=40
        )
        Listing.objects.create(
            neighbourhood_group="Manchester",
            neighbourhood="Piccadilly",
            latitude=53.4401,
            longitude=-2.28187,
            price=12
        )
        Listing.objects.create(
            neighbourhood_group="Manchester",
            neighbourhood='Deansgate',
            latitude=53.4394,
            longitude=2.28205,
            price=20
        )

    def test_outcode_view(self):
        response = self.client.get('http://127.0.0.1:8000/api/outcode/M1/')
        response2 = self.client.get('http://127.0.0.1:8000/api/outcode/DA1/')
        self.assertEqual(26, response.data.get('average_daily_price'))
        self.assertEqual(4, response.data.get('listing_count'))
        self.assertEqual(404, response2.status_code)
    
    def test_nexus_outcode_view(self):
        response = self.client.get('http://127.0.0.1:8000/api/nexus/M1/')
        response2 = self.client.get('http://127.0.0.1:8000/api/outcode/DA1/')
        outcodes = response.data.get('outcodes')
        self.assertEqual(26, response.data.get('average_daily_price'))
        self.assertEqual(4, response.data.get('listing_count'))
        self.assertEqual(404, response2.status_code)

        # test averages for M2 outcode
        self.assertEqual(16, outcodes[0].get('average_daily_price'))
        # test averages for M15 outcode
        self.assertEqual(31, outcodes[6].get('average_daily_price'))



