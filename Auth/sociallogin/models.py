# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class SocialLoginUser(models.Model):
    provider = models.CharField(max_length=20)
    email=models.EmailField()

    def __str__(self):
        return  self.email


