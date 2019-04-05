# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from serializers.vendors import VendorSerializer
from vendors.models import Vendor
from vendors.permissions import IsOwnerOrReadOnly


class VendorsList(APIView):
    """
    List all Vendors, or create a new vendor.
    """
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get(self, request, format=None):
        """HTTP GET method."""

        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """HTTP POST method."""
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.owner = request.user.id
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendorsDetail(APIView):
    """
     Retrieve, update or delete a vendor instance.
    """
    def get_object(self, pk):
        try:
            return Vendor.objects.get(pk=pk)
        except Vendor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """HTTP GET method."""
        vendor = self.get_object(pk=pk)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """HTTP PUT method."""
        vendor = self.get_object(pk=pk)
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """HTTP DELETE method."""
        vendor = self.get_object(pk=pk)
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
