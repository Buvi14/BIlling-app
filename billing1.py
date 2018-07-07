# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 22:13:36 2018

@author: Buvaneshkumar R
"""

class BaseBillingDetailsView(FormView):
    def get_success_url(self):
        return self.request.path
    def form_valid(self, form):
        ba = self.request.user.billing_account             # let billing processor save details
        form.billing_account = ba
        form.save()                                       # do redirect (or do more processing by ignoring return value)
        return super(BaseBillingDetailsView, self).form_valid(form)

class BaseSubscriptionView(BaseBillingDetailsView):
    def get_context_data(self, **kwargs):                 # Call the base implementation first to get a context
        context = super(BaseSubscriptionView, self).get_context_data(**kwargs)
        product = billing.loading.get_product(self.kwargs['product'])
        context['product'] = product
        return context
    def form_valid(self, form):
        response = super(BaseSubscriptionView, self).form_valid(form)

        ba = self.request.user.billing_account            # create subscription
        ba.subscribe_to_product(self.kwargs['product'])   # return the redirect
        return response