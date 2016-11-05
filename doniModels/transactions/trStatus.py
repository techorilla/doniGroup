from django.db import models
from datetime import date
from django.contrib.auth.models import User
from .trBasic import Transaction


class TrStatus(models.Model):
    ALL_STATUS = (
        ('Washout at Par', 'WASHOUT_AT_PAR'),
        ('Arrived', 'ARRIVED'),
        ('Shipped', 'SHIPPED'),
        ('Washout at X', 'WASHOUT_AT_X'),
        ('Completed', 'COMPLETED'),
        ('Not Shipped', 'NOT_SHIPPED')
    )
    transaction = models.OneToOneField(
        Transaction,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    status = models.CharField(
        max_length=50,
        choices=ALL_STATUS,
        default='Not Shipped',
        blank=False
    )
    washout_at_par = models.FloatField(null=True)
    createdOn = models.DateField(default=date.today)
    updatedOn = models.DateField(default=None)
    createdBy = models.ForeignKey(User,
                                  null=False,
                                  blank=False,
                                  related_name='tr_status')
    updatedBy = models.ForeignKey(User,
                                  null=False,
                                  blank=False,
                                  related_name='tr_status')

    class Meta:
        db_table = 'tr_status'
