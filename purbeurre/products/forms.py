from django import forms

class SearchedProductForm(forms.Form):
    query_search = forms.CharField(label="",
                                    max_length=255,
                                    widget=forms.TextInput(
                                        attrs={
                                            'class':'product_search',
                                            }))