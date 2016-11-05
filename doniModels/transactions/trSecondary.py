from django.db import models
from datetime import date
from django.contrib.auth.models import User
from .trBasic import Transaction
from ..businessPartner import BpBasic

class SecondaryTransaction(models.Model):
    transaction = models.ForeignKey(
        Transaction,
        on_delete=models.CASCADE
    )
    tr_sec_id = models.AutoField(primary_key=True)
    date = models.DateField(default=date.today)
    buyer = models.ForeignKey(BpBasic, null=True, related_name='tr_secondary')
    seller = models.ForeignKey(BpBasic, null=True, related_name='tr_secondary')
    buyer_price = models.FloatField(default=0.00)
    seller_price = models.FloatField(default=0.00)
    other_info = models.TextField()
    quantity = models.FloatField(default=0.00)


    class Meta:
        db_table = 'tr_secondary'
