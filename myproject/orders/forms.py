from django import forms
from django.utils.translation import ugettext_lazy as _
from orders.models import ODOrder


class ODOrderForm(forms.ModelForm):
    """
    Form to manage Order data-entry
    """
    name = forms.CharField(label=_('Customers'))

    class Meta:
        model = ODOrder
        fields = ('name','email', 'phone', 'address', 'images')

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
    )
