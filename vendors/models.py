# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core import serializers
from django.db import models

from base.models import BaseModel


class Vendor(BaseModel):
    owner = models.ForeignKey("auth.User", related_name="vendors", on_delete=models.CASCADE)
    cnpjcpf = models.CharField(max_length=16)

    @property
    def json(self):
        return serializers.serialize('json', [ self, ])
