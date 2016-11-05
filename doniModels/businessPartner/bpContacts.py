from django.db import models
from datetime import date
from django.contrib.auth.models import User
from .bpBasic import BpBasic


class BpContact(models.Model):
    bp_id = models.ForeignKey(BpBasic,
                              null=False,
                              blank=False,
                              related_name='bp_contact_number')
    id = models.AutoField(primary_key=True)
    is_primary = models.BooleanField(default=False)
    full_name = models.CharField(max_length=100, null=False, blank=False)
    designation = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=300, unique=True, null=True)
    primary_number = models.CharField(max_length=100, null=True)
    secondary_number = models.CharField(max_length=100, null=True)

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
