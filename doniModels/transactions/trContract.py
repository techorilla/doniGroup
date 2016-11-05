from django.db import models
from datetime import date
from django.contrib.auth.models import User
from .trBasic import Transaction
from ..businessPartner import BpBasic


class TrContract(models.Model):
    transaction = models.OneToOneField(
        Transaction,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    doni_contract = models.BooleanField(default=False)
    own_contract = models.BooleanField(default=False)
    contractual_buyer = models.ForeignKey(BpBasic, null=True, related_name='tr_contract')

    createdOn = models.DateField(default=date.today)
    updatedOn = models.DateField(default=None)
    createdBy = models.ForeignKey(User,
                                  null=False,
                                  blank=False,
                                  related_name='tr_contract')
    updatedBy = models.ForeignKey(User,
                                  null=False,
                                  blank=False,
                                  related_name='tr_contract')

    class Meta:
        db_table = 'tr_contract'
