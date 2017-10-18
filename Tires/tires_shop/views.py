from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.template.response import TemplateResponse
from django.urls import reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.core.mail import EmailMessage
from django.template import Context
from django.views.generic import DeleteView
from django.views.generic import UpdateView

from .forms import LoginForm, TireSearchForm, NewTireForm, SignUpForm, ContactForm
from .models import Tires


class TiresView(View):
    def get(self, request):
        return render(request, 'base.html')


class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['login'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('start'))
            else:
                return HttpResponse('Niepoprawne dane logowania')


class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))


class TiresListView(View):
    def get(self, request):
        return TemplateResponse(request, 'tires.html')


class TireSearchView(View):
    def get(self, request):
        form = TireSearchForm()
        return render(request, 'tire_search.html', {'form': form})

    def post(self, request):
        form = TireSearchForm(request.POST)
        if form.is_valid():
            brand = form.cleaned_data['brand']
            tire = Tires.objects.filter(Q(price__icontains=brand) |
                                        Q(width__icontains=brand) |
                                        Q(tire_brand__icontains=brand) |
                                        Q(aspect_ratio__icontains=brand) |
                                        Q(diameter__icontains=brand)).distinct()
            return render(request, 'tire_search.html', {'form': form, 'tire': tire})


class NewTireView(CreateView):
    form_class = NewTireForm
    template_name = 'new_tire.html'
    success_url = reverse_lazy('start')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('start')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
                , '')
            contact_email = request.POST.get(
                'contact_email'
                , '')
            form_content = request.POST.get('content', '')

            template = get_template('contact_template.txt')
            ctx = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(ctx)

            email = EmailMessage(
                "Customer's help request",
                content,
                "Tire's website" + '',
                ["Owner's e-mail"],
            )
            email.send()
            return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })


class TireUpdate(UpdateView):
    model = Tires
    template_name = 'update_tire.html'
    success_url = reverse_lazy('list')
    fields = ['width', 'aspect_ratio', 'diameter', 'tire_brand', 'tire_model', 'production_month', 'production_year',
              'season_type', 'type_of_load', 'price', 'quantity', 'image']


class TireDelete(DeleteView):
    model = Tires
    template_name = 'delete_tire.html'
    success_url = reverse_lazy('list')
