from django import forms


class SearchedProduct(forms.Form):
    search = forms.CharField(widget=forms.Textarea, max_length=255)

    def cleaned_data(self):
        data = self.cleaned_data['search']
        return data