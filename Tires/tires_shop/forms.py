from django import forms


class LoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class TireSearchForm(forms.Form):
    brand = forms.CharField(label='Search')
