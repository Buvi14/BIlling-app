from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse
from django.http import Http404

import billing.loading
import billing.processor
from billing.forms import SubscriptionConfirmationForm
from billing.models import Subscription, ProductType


class BillingOverviewView(TemplateView):
    template_name = 'billing/overview.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BillingOverviewView, self).get_context_data(**kwargs)
        # Add in a list of all the products
        context['all_products'] = billing.loading.get_products(hidden=True)
        context['public_products'] = billing.loading.get_products()
        billing_account = self.request.user.billing_account
        context['billing_account'] = billing_account
        context['products'] = billing_account.get_visible_products()
        current_product = billing_account.get_current_product_class()
        context['current_product'] = current_product
        return context