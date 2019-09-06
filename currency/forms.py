from django import forms

# dummy choices 
choices=INTEGER_CHOICES = [('', '')]

class CurrencyForm(forms.Form):
    source_currency_value = forms.DecimalField(label='Amount')
    source_currency_code = forms.CharField(label='From', widget = forms.Select(choices=INTEGER_CHOICES))
    target_currency_code = forms.CharField(label='To', widget = forms.Select(choices=INTEGER_CHOICES))


    def __init__(self, tuple_country_code, *args, **kwargs):
        # required to set the initial form drop down with choices
        self.tuple_country_code = tuple_country_code
        super(CurrencyForm,self).__init__(*args, **kwargs)

        self.fields['source_currency_code'].widget.choices = self.tuple_country_code
        self.fields['target_currency_code'].widget.choices = self.tuple_country_code