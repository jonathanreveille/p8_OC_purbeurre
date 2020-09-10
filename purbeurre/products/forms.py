from django import forms

class SearchedProduct(forms.Form):
    search = forms.CharField(label='trouver un produit', max_length=255) 