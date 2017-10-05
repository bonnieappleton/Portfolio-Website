from django import forms

class PageAnalyserForm(forms.Form):
    url = forms.URLField(
        required=True,
        label='URL',
    )