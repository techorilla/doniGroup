from django.db import models
from datetime import date
from django.contrib.auth.models import User
from .trBasic import Transaction
from ..businessPartner import BpBasic
from ..ports import Port


class TrShipment(models.Model):
    models.OneToOneField(
        Transaction,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    not_shipped = models.BooleanField(default=False)
    not_shipped_reason = models.TextField()
    extension = models.CharField(max_length=100)
    app_received = models.BooleanField(default=False)
    expected_shipment = models.DateField(default=None)
    in_transit = models.DateField(default=None)
    shipped = models.BooleanField(default=False)
    date_arrived = models.DateField(default=None)
    expected_arrival = models.DateField(default=None)
    transit_port = models.CharField(max_length=500, null=True)
    arrived_at_port = models.BooleanField(default=False)
    date_arrived = models.DateField(default=None)
    actual_arrived = models.DateField(default=None)
    bl_no = models.CharField(max_length=50, null=True)
    invoice_no = models.CharField(max_length=50)
    invoice_amount = models.FloatField(null=True)
    quantity = models.FloatField(null=True)
    vessel_no = models.CharField(max_length=50)
    shipper_id = models.ForeignKey(BpBasic, null=True, related_name='tr_shipment')
    port_loading = models.ForeignKey(Port, null=True, related_name='tr_shipment')
    port_destination = models.ForeignKey(Port, null=True, related_name='tr_shipment')
    ship_line_details = models.TextField()
    chk_reason = models.BooleanField(default=False)
    chk_ship_ext = models.BooleanField(default=False)
    chk_exp_ship = models.BooleanField(default=False)
    chk_in_transit = models.BooleanField(default=False)
    chk_date_shipped = models.BooleanField(default=False)
    chk_expected_arrival = models.BooleanField(default=False)
    chk_transit_port = models.BooleanField(default=False)
    chk_date_arrived = models.BooleanField(default=False)
    chk_actual_arrived = models.BooleanField(default=False)
    createdOn = models.DateField(default=date.today)
    updatedOn = models.DateField(default=None)
    createdBy = models.ForeignKey(User,
                                  null=False,
                                  blank=False,
                                  related_name='tr_shipment')
    updatedBy = models.ForeignKey(User,
                                  null=True,
                                  blank=False,
                                  related_name='tr_shipment')

    class Meta:
        db_table = 'tr_shipment'
