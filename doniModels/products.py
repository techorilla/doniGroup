from django.db import models
from datetime import date
from django.contrib.auth.models import User
from .origins import Origin


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    moisture = models.FloatField(default=None)
    purity = models.FloatField(default=None)
    weaveled = models.FloatField(default=None)
    origin = models.ForeignKey(Origin,
                               null=False,
                               blank=False,
                               related_name='products')
    splits = models.FloatField(default=None)
    quality = models.FloatField(default=None)
    damaged = models.FloatField(default=None)
    foreignMatter = models.FloatField(default=None)
    greenDamaged = models.FloatField(default=None)
    otherColor = models.FloatField(default=None)
    wrinkled = models.FloatField(default=None)
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
        db_table = 'products'

    def __unicode__(self):
        return self.name
