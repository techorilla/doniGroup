from django.db import models
from datetime import date
from django.contrib.auth.models import User


class BpBasic(models.Model):
    bp_id = models.AutoField(primary_key=True)
    bp_name = models.CharField(max_length=500, null=False, blank=False)
    bp_website = models.CharField(max_length=500, null=False, blank=False)
    bp_credibility_index = models.IntegerField(default=1)
    bp_country = models.CharField(max_length=250, null=True)
    bp_address = models.CharField(max_length=1000, null=True, blank=True)
    bp_is_buyer = models.BooleanField(default=False)
    bp_is_seller = models.BooleanField(default=False)
    bp_is_shipper = models.BooleanField(default=False)
    bp_is_broker = models.BooleanField(default=False)
    bp_on_contract = models.BooleanField(default=False)
    createdOn = models.DateField(default=date.today)
    updatedOn = models.DateField(default=None)
    createdBy = models.ForeignKey(User,
                                  null=False,
                                  blank=False,
                                  related_name='bp_basic')
    updatedBy = models.ForeignKey(User,
                                  null=False,
                                  blank=False,
                                  related_name='bp_basic')

    class Meta:
        db_table = 'bp_basic'
