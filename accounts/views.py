from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.core.urlresolvers import reverse_lazy

# Create your views here.
from django.views.generic import TemplateView, UpdateView, FormView

class IndexView(LoginRequiredMixin, TemplateView):

    template_name = 'accounts/index.html'

index = IndexView.as_view()

class UpadateUserView(LoginRequiredMixin, UpdateView):

    model = User
    template_name = 'accounts/updateuser.html'
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('accounts:index')

    def get_object(self):
        return self.request.user

update_user = UpadateUserView.as_view()

class UpdatePasswordView(FormView):

    template_name = 'accounts/update_password.html'
    success_url = reverse_lazy('accounts:index')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(UpdatePasswordView, self).form_valid(form)

update_password = UpdatePasswordView.as_view()
