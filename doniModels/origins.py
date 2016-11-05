from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Origin(models.Models):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    createdOn = models.DateField(default=date.today)
    updatedOn = models.DateField(default=None)
    createdBy = models.ForeignKey(User,
                                  null=False,
                                  blank=False,
                                  related_name='origins')
    updatedBy = models.ForeignKey(User,
                                  null=False,
                                  blank=False,
                                  related_name='origins')

    class Meta:
        db_table = 'origins'

    def __unicode__(self):
        return self.name
