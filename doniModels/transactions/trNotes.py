from django.db import models
from datetime import date
from django.contrib.auth.models import User
from .trBasic import Transaction


class TrNotes(models.Model):
    transaction = models.ForeignKey(
        Transaction,
        on_delete=models.CASCADE
    )
    note_id = models.AutoField(primary_key=True)
    note = models.TextField()

    createdOn = models.DateField(default=date.today)
    updatedOn = models.DateField(default=None)
    createdBy = models.ForeignKey(User,
                                  null=False,
                                  blank=False,
                                  related_name='tr_notes')
    updatedBy = models.ForeignKey(User,
                                  null=False,
                                  blank=False,
                                  related_name='tr_notes')

    class Meta:
        db_table = 'tr_notes'
