from django.db import models
from datetime import date
from django.contrib.auth.models import User
from ..businessPartner.bpBasic import BpBasic
from ..products import Products
from ..origins import Origin


class Transaction(models.Model):
    tr_id = models.AutoField(primary_key=True)
    date = models.DateField(default=date.today)
    buyer = models.ForeignKey(BpBasic, null=False, related_name='tr_basic')
    seller = models.ForeignKey(BpBasic, null=False, related_name='tr_basic')
    product = models.ForeignKey(Products, null=False, related_name='tr_basic')
    origin = models.ForeignKey(Origin, null=False, related_name='tr_basic')
    quantity = models.FloatField(default=None)
    price = models.FloatField(default=None)
    packing = models.CharField(max_length=50)
    shipment_start = models.DateField()
    shipment_end = models.DateField()
    file_id = models.CharField(null=False, unique=True, blank=False)
    contract_id = models.CharField(null=True)
    other_info = models.CharField(null=True, blank=True)
    createdOn = models.DateField(default=date.today)
    updatedOn = models.DateField(default=None)
    createdBy = models.ForeignKey(User,
                                  null=False,
                                  blank=False,
                                  related_name='tr_basic')
    updatedBy = models.ForeignKey(User,
                                  null=False,
                                  blank=False,
                                  related_name='tr_basic')

    class Meta:
        db_table = 'tr_basic'
