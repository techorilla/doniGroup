from django.db import models
from django.contrib.auth.models import User
from .products import Products


class DashboardProduct(models.Models):
    product = models.ForeignKey(Products, null=False, )
    user = models.ForeignKey(User, null=False, related_name='dashboard_product')

    class Meta:
        db_table = 'dashboard_product'

    def __unicode__(self):
        return self.name
