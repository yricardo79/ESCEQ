from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.views.generic import RedirectView


class LoginESCEQView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar Sesión'
        return context




""" NO
class LogoutESCEQView(RedirectView):
    pattern_name = 'login'

    def dispatch(self, request, *args, **kwargs):
        #cierra la sesión
        logout(request)
        #redirecciona
        return super().dispatch(self, request, *args, **kwargs)
"""