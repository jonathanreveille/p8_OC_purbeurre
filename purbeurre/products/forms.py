from django import forms

class SearchedProduct(forms.Form):
    query_search = forms.CharField(label='trouver un produit', max_length=255)