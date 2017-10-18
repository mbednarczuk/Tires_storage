from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views import View

from .forms import LoginForm, TireSearchForm
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
