from django import forms


class QueryForm(forms.Form):
    query = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'input is-rounded',
        'placeholder': 'Например: cats',
    }))
