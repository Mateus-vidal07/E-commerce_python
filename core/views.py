## -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from catalog.models import Category
from .forms import ContactForm, RegisterForm

User = get_user_model()
# Create your views here.
class IndexView(TemplateView):

    template_name = 'index.html'

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_mail()

            messages.success(request, 'Obrigado! sua mensagem foi enviada corretamente')
        else:
            messages.error(request, 'O formulario não é valido, por favor preencha os campos corretamente')
    else:
        form = ContactForm()
    context = {
        'form':form,
    }
    return render(request, 'contact.html', context)

#chamando as viewa
index = IndexView.as_view()

#criando a pagina de registração
class RegisterView(CreateView):

    form_class = RegisterForm
    template_name = 'register.html'
    model = User
    success_url = reverse_lazy('login')

register = RegisterView.as_view()
