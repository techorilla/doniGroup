from django.db import models
from datetime import date
from django.contrib.auth.models import User
from .bpBasic import BpBasic
from ..products import Products


class BpProducts(models.Model):
    bp_id = models.ForeignKey(BpBasic,
                              null=False,
                              blank=False,
                              related_name='bp_products')
    product_id = models.ForeignKey(Products,
                                   null=False,
                                   blank=False,
                                   related_name='bp_products')

    createdOn = models.DateField(default=date.today)
    updatedOn = models.DateField(default=None)
    createdBy = models.ForeignKey(User,
                                  null=False,
                                  blank=False,
                                  related_name='bp_products')
    updatedBy = models.ForeignKey(User,
                                  null=False,
                                  blank=False,
                                  related_name='bp_products')

    class Meta:
        db_table = 'bp_products'
