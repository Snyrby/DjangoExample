from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Your Title'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': 'Your Description',
                                                                               'class': 'new-class-name two',
                                                                               'id': 'my-id-for-text area', 'rows': 20,
                                                                               'cols': 120})),
    active = forms.BooleanField(initial=True, required=False)
    class Meta:
        model = Article
        fields = ['title', 'description', 'active']
