from django import forms
from .models import course

class CourseModelForm(forms.ModelForm):
    class Meta:
        model = course
        fields = ['title']
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.lower() == 'abc':
            raise forms.ValidationError('This is not a valid title')
        return title
