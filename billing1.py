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
        return context
class BillingDetailsView(BaseBillingDetailsView):         #show the billing detials
    template_name = 'billing/details.html'
    def get_form_class(self):
        billing_account = self.request.user.billing_account
        processor = billing_account.get_processor()
        return processor.get_billing_details_form(billing_account)
class BillingHistoryView(TemplateView):                  #main function
    template_name = 'billing/history.html'
    pass
    def dispatch(request, *args, **kwargs):
        cur_product_cls = request.user.billing_account.get_current_product_class()
        req_product_name = kwargs['product']
        try:
            req_product_cls = billing.loading.get_product(req_product_name)
        except ValueError:
            raise Http404
        if req_product_cls not in request.user.billing_account.get_visible_products():
            raise Http404
        if (req_product_cls.get_requires_payment_details()and not request.user.billing_account.has_valid_billing_details()):
            return billing_details_view(request, *args, **kwargs)
        elif (
            not req_product_cls.get_requires_payment_details()
            or request.user.billing_account.has_valid_billing_details()
        ):
            return confirmation_view(request, *args, **kwargs)
        else:
            raise RuntimeError('Error: null condition should never occur')
     return dispatch