from django.db import models
from datetime import date
from django.contrib.auth.models import User
from .bpBasic import BpBasic


class BpContactNumber(models.Model):
    bp_id = models.ForeignKey(BpBasic,
                              null=False,
                              blank=False,
                              related_name='bp_contact_number')

    id = models.AutoField(primary_key=True)
    contact_number = models.CharField(max_length=300, null=False, unique=True)
    type = models.CharField(max_length=50)
    createdOn = models.DateField(default=date.today)
    updatedOn = models.DateField(default=None)
    createdBy = models.ForeignKey(User,
                                  null=False,
                                  blank=False,
                                  related_name='bp_contact_number')
    updatedBy = models.ForeignKey(User,
                                  null=False,
                                  blank=False,
                                  related_name='bp_contact_number')

    class Meta:
        db_table = 'bp_contact_number'
