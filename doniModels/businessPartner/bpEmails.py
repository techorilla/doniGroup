from django.db import models
from datetime import date
from django.contrib.auth.models import User
from .bpBasic import BpBasic


class BpEmail(models.Model):
    bp_id = models.ForeignKey(BpBasic,
                              null=False,
                              blank=False,
                              related_name='bp_emails')
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=300, unique=True, null=False)
    createdOn = models.DateField(default=date.today)
    updatedOn = models.DateField(default=None)
    createdBy = models.ForeignKey(User,
                                  null=False,
                                  blank=False,
                                  related_name='bp_emails')
    updatedBy = models.ForeignKey(User,
                                  null=False,
                                  blank=False,
                                  related_name='bp_emails')

    class Meta:
        db_table = 'bp_emails'
