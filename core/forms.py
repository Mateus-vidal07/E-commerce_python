## -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.conf import settings

class ContactForm(forms.Form):

    name = forms.CharField(label='Nome', help_text='coloque um nome')
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'placeholder':'Mensagem'}))


    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['email'].help_text = 'Letras minusculas'

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        messagess = 'Nome: {}\n Email: {}\n Message: {}'.format(name, email, message)
        send_mail('Assunto', messagess, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])

class RegisterForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = {
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        }

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
