# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 23:47:11 2018

@author: Buvaneshkumar R
"""

class BillingDetailsView(BaseBillingDetailsView):
    template_name = 'billing/details.html'
    def get_form_class(self):
        billing_account = self.request.user.billing_account
        processor = billing_account.get_processor()
        return processor.get_billing_details_form(billing_account)