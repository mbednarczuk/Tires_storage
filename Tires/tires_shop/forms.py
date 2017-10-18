from django import forms

from tires_shop.models import Tires


class LoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class TireSearchForm(forms.Form):
    brand = forms.CharField(label='Search')


class NewTireForm(forms.ModelForm):
    class Meta:
        model = Tires
        fields = '__all__'
