from django import forms


class ArticleSharingForm(forms.Form):
    url = forms.URLField(label='Article\'s url')
