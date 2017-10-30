# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.db import models
from django import forms


class Users(models.Model):

    email=models.EmailField()
    password=models.CharField(max_length=20)
    confirmpassword=models.CharField(max_length=20)


    def __str__(self):
       return (self.email)












