from django.contrib.auth.models import User

from rest_framework import serializers

from vendors.models import Vendor

class UserSerializer(serializers.ModelSerializer):
    vendors = serializers.PrimaryKeyRelatedField(many=True, queryset=Vendor.objects.all())

    class Meta:
        model = User
        fields = ("id", "username", "vendors")
