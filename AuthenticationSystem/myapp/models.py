# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Users(models.Model):
    email = models.EmailField();
    password = models.CharField(max_length=20);

    # token=models.CharField(max_length=500);
    # provider = models.CharField(max_length=50);

    def __str__(self):
        return self.email;



