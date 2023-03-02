from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Your Title'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': 'Your Description',
                                                                               'class': 'new-class-name two',
                                                                               'id': 'my-id-for-text area', 'rows': 20,
                                                                               'cols': 120}))
    price = forms.DecimalField(initial=199.99)
    class Meta:
        model = Product
        fields = ['title', 'description', 'price']


class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Your Title'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'new-class-name two',
                                                                               'id': 'my-id-for-textarea', 'rows': 20,
                                                                               'cols': 120}))
    price = forms.DecimalField()
