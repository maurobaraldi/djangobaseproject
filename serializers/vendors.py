from rest_framework import serializers

from vendors.models import Vendor

class VendorSerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Vendor
        fields = ("owner", "cnpjcpf", "created_at", "updated_at")
