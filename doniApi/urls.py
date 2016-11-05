from doniApi import *
from django.conf.urls import include, url

'''
    All Data API for Doni Group
'''

urlpatterns = (

    # Business Partner Related API

    url(r'bp_partner/basic/(?P<bp_id>[a-zA-Z0-9.@_-]+)/$',
        BpBasicAPI.as_view(),
        name='Business Partner Basic'),

    url(r'bp_partner/(?P<bp_id>[a-zA-Z0-9.@_-]+)/bank/(?P<bank_id>[a-zA-Z0-9.@_-]+)/$',
        BpContactNumberAPI.as_view(),
        name='Business Partner Basic'),

    url(r'bp_partner/(?P<bp_id>[a-zA-Z0-9.@_-]+)/contact_number/(?P<cn_id>[a-zA-Z0-9.@_-]+)/$',
        BpContactNumberAPI.as_view(),
        name='Business Partner Contact Number'),

    url(r'bp_partner/(?P<bp_id>[a-zA-Z0-9.@_-]+)/contact_person/(?P<cp_id>[a-zA-Z0-9.@_-]+)/$',
        BpContactNumberAPI.as_view(),
        name='Business Partner Person'),

    url(r'bp_partner/(?P<bp_id>[a-zA-Z0-9.@_-]+)/products/(?P<product_id>[a-zA-Z0-9.@_-]+)/$',
        BpProductsAPI.as_view(),
        name='Business Partner Products'),

    # Transaction Related API

    url(r'transactions/(?P<tr_id>[a-zA-Z0-9.@_-]+)/basic/$',
        TransactionBasicAPI.as_view(),
        name='Transaction Basic'),

    url(r'transactions/(?P<tr_id>[a-zA-Z0-9.@_-]+)/commission/$',
        TransactionCommissionAPI.as_view(),
        name='Transaction Commission'),

    url(r'transactions/(?P<tr_id>[a-zA-Z0-9.@_-]+)/contract/$',
        TransactionContractAPI.as_view(),
        name='Transaction Contract'),

    url(r'transactions/(?P<tr_id>[a-zA-Z0-9.@_-]+)/document/(?P<doc_id>[a-zA-Z0-9.@_-]+)$',
        TransactionNoteAPI.as_view(),
        name='Transaction Documents'),

    url(r'transactions/(?P<tr_id>[a-zA-Z0-9.@_-]+)/note/(?P<bp_id>[a-zA-Z0-9.@_-]+)/$',
        TransactionBasicAPI.as_view(),
        name='Transaction Notes'),

    url(r'transactions/(?P<tr_id>[a-zA-Z0-9.@_-]+)/secondary/(?P<sec_id>[a-zA-Z0-9.@_-]+)$',
        TransactionSecondaryAPI.as_view(),
        name='Transaction Secondary'),

    url(r'transactions/(?P<tr_id>[a-zA-Z0-9.@_-]+)/status/$',
        TransactionBasicAPI.as_view(),
        name='Transaction Status'),

    url(r'transactions/(?P<tr_id>[a-zA-Z0-9.@_-]+)/shipment/$',
        TransactionShipmentAPI.as_view(),
        name='Transaction Shipment'),

    # Reports Related API

    # Manifest Related API

    # Product Pricing API

    # Origins API

    # Product Related API

    url(r'product/(?P<product_id>[a-zA-Z0-9.@_-]+)',
        BpProductsAPI.as_view(),
        name='Products')

)
