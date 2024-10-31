from django import forms
from .models import Url


class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ['url']

    def clean_url(self):
        url = self.cleaned_data['url']
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        return url
