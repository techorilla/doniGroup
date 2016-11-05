from django.db import models
from datetime import date
from django.contrib.auth.models import User
from .trBasic import Transaction


class TrFiles(models.Model):
    transaction = models.ForeignKey(
        Transaction,
        on_delete=models.CASCADE
    )
    file_id = models.AutoField(primary_key=True)
    file = models.BinaryField()
    createdOn = models.DateField(default=date.today)
    updatedOn = models.DateField(default=None)
    createdBy = models.ForeignKey(User,
                                  null=False,
                                  blank=False,
                                  related_name='tr_files')
    updatedBy = models.ForeignKey(User,
                                  null=False,
                                  blank=False,
                                  related_name='tr_files')

    class Meta:
        db_table = 'tr_notes'
