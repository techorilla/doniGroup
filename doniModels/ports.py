from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Port(models.Models):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    createdOn = models.DateField(default=date.today)
    updatedOn = models.DateField(default=None)
    createdBy = models.ForeignKey(User,
                                  null=False,
                                  blank=False,
                                  related_name='products')
    updatedBy = models.ForeignKey(User,
                                  null=False,
                                  blank=False,
                                  related_name='products')


    class Meta:
        db_table = 'port'