# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class VendorTests(APITestCase):
    """Vendors API test case."""

    def setUp(self):
        """SetUp test class."""
        User.objects.create_superuser("john",  "john@snow.com", "thenorthremembers")
        self.client.login(username="john", password="thenorthremembers")

    def test_list_vendors(self):
        """Test list vendors API should succeed."""
        response = self.client.get(reverse("vendor"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_insert_vendors(self):
        """Test create vendor registry API should succeed."""
      response = self.client.post(reverse("vendor"), data={"cnpjcpf": "1234567890"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
