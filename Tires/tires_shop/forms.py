from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from tires_shop.models import Tires, Order, BrandsDescribe


class LoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class TireSearchForm(forms.Form):
    brand = forms.CharField(label='Search')


class NewTireForm(forms.ModelForm):
    class Meta:
        model = Tires
        fields = '__all__'


class NewBrandForm(forms.ModelForm):
    class Meta:
        model = BrandsDescribe
        fields = '__all__'


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='You do not have to, but It would be nice.')
    last_name = forms.CharField(max_length=30, required=False, help_text='You do not have to, but It would be nice.')
    email = forms.EmailField(max_length=254, help_text='This what we really need :)')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Contact email:"
        self.fields['content'].label = "How can I help You?"


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput())
    new_password_2 = forms.CharField(widget=forms.PasswordInput())


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('order_tire', 'quantity')
