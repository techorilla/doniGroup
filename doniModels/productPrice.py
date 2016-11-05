from django.db import models
from django.contrib.auth.models import User
from .products import Products
from datetime import date


class ProductPrice(models.Models):
    product = models.ForeignKey(Products, null=False, )
    local_price = models.FloatField(default=0.00)
    international_price = models.FloatField(default=0.00)
    date = models.DateField(default=date.today)
    createdOn = models.DateField(default=date.today)
    updatedOn = models.DateField(default=None)
    createdBy = models.ForeignKey(User,
                                  null=False,
                                  blank=False,
                                  related_name='product_price')
    updatedBy = models.ForeignKey(User,
                                  null=False,
                                  blank=False,
                                  related_name='product_price')

    class Meta:
        db_table = 'product_price'

    def __unicode__(self):
        return self.name
