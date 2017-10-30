# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UserSocial (models.Model):
    email=models.EmailField()
    provider = models.CharField(max_length=20)
    # userId=models.CharField(max_length=50)

    def __str__(self):
        return self.email

