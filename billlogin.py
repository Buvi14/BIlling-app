# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 23:51:32 2018

@author: Buvaneshkumar R
"""
from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.decorators import login_required

from billing.views import BillingOverviewView
from billing.views import BillingHistoryView, BillingDetailsView

urlpatterns = patterns('',
    url(r'^$', login_required(BillingOverviewView.as_view()), name='billing_overview'),
    url(r'^history/$',login_required(BillingHistoryView.as_view()),name='billing_history'),
    url(r'^details/$',login_required(BillingDetailsView.as_view()),name='billing_details'),
)