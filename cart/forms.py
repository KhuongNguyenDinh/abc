from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]

class CartAddProductForm(forms.Form):
    quantity = forms.ChoiceField(choices=PRODUCT_QUANTITY_CHOICES, widget=forms.Select(attrs={'class':'form-control','style':'width: 90px; text-align:center'}))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
