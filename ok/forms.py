from django import forms

class ScanForm(forms.Form):
    target = forms.CharField(max_length=100,label='', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Entrer une adresse...'
    }))
