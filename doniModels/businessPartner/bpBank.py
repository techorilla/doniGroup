from django.db import models
from datetime import date
from django.contrib.auth.models import User
from .bpBasic import BpBasic


class BpBank(models.Model):
    bp_id = models.ForeignKey(BpBasic,
                              null=False,
                              blank=False,
                              related_name='bp_bank')
    acc_id = models.AutoField(primary_key=True)
    branch_address = models.CharField(max_length=250, null=False, blank=False)
    bank_name = models.CharField(max_length=100, null=False)
    acc_title = models.CharField(max_length=150, null=False)
    acc_number = models.CharField(max_length=100, null=False)
    acc_country = models.CharField(max_length=250, null=False)
    createdOn = models.DateField(default=date.today)
    updatedOn = models.DateField(default=None)
    createdBy = models.ForeignKey(User,
                                  null=False,
                                  blank=False,
                                  related_name='bp_bank')
    updatedBy = models.ForeignKey(User,
                                  null=False,
                                  blank=False,
                                  related_name='bp_bank')

    class Meta:
        db_table = 'bp_bank'