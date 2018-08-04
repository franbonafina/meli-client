import json
import melipy.meliresources as meliresources
from melipy.core import MeliCore
from urllib.parse import urlparse, parse_qs, urlsplit, urlencode, urljoin
from django.contrib import messages
from django.contrib.auth import login, authenticate, REDIRECT_FIELD_NAME
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.utils.crypto import get_random_string
from django.utils.decorators import method_decorator
#from django.utils.http import is_safe_url
from django.utils.encoding import force_bytes
#from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import View, FormView
from django.conf import settings

from .forms import (SignInViaEmailForm, SignUpForm, RemindUsernameForm, ChangeProfileForm)
from django.contrib.auth.views import (LogoutView as BaseLogoutView)
from .models import Activation


class GuestOnlyView(View):
    def dispatch(self, request, *args, **kwargs):
        # Redirect to the index page if the user already authenticated
        if request.user.is_authenticated:
            # Server meli 'code' response parse to obtain ACCES_TOKEN 
            url = request.get_full_path()        
            query = url.split('?',1)[-1]
            code = query.split('=',1)[-1]            
            #meli = MeliCore(client_id=settings.CLIENT_ID,client_secret=settings.CLIENT_SECRET)
            #meli.authorize(code, urlparse('localhost').geturl()) ## HERE ERROR WITH ENCODING :=%3A 
            return redirect(settings.LOGIN_REDIRECT_URL)

        return super().dispatch(request, *args, **kwargs)


class LogInView(GuestOnlyView, FormView):
    template_name = 'accounts/log_in.html'

    @staticmethod
    def get_form_class(**kwargs):
        if settings.LOGIN_VIA_EMAIL:
            return SignInViaEmailForm

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        request = self.request

        # If the test cookie worked, go ahead and delete it since its no longer needed
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()

        # The default Django's "remember me" lifetime is 2 weeks and can be changed by modifying
        # the SESSION_COOKIE_AGE settings' option.
        if settings.USE_REMEMBER_ME:
            if not form.cleaned_data['remember_me']:
                request.session.set_expiry(0)

        login(request, form.user_cache)

        """
        #To make external redirection ? .
        redirect_to = request.POST.get(REDIRECT_FIELD_NAME, request.GET.get(REDIRECT_FIELD_NAME))
        url_is_safe = is_safe_url(redirect_to, allowed_hosts=request.get_host(), require_https=request.is_secure())
        if url_is_safe:
            return redirect(redirect_to)
        """
        meli = MeliCore(client_id=settings.CLIENT_ID,client_secret=settings.CLIENT_SECRET)
        auth_url = meli.get_auth_url(redirect_URI=settings.LOGIN_REDIRECT_URL)

        return redirect(auth_url)


class SignUpView(GuestOnlyView, FormView):
    template_name = 'accounts/sign_up.html'
    form_class = SignUpForm

    def form_valid(self, form):
        request = self.request
        user = form.save(commit=False)

        user.username = form.cleaned_data['username']

        if settings.ENABLE_USER_ACTIVATION:
            user.is_active = True

        # Create a user record
        user.save()

        # Change the username to the "user_ID" form
        if settings.ENABLE_USER_ACTIVATION:
            code = get_random_string(20) #Id mercadoLibre
            act = Activation()
            act.code = code
            act.user = user
            act.save()       
            messages.success(
                request, _('You are signed up.'))
        else:
            raw_password = form.cleaned_data['password1']

            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            messages.success(request, _('You are successfully signed up!'))

        return redirect('index')


class CreateNewPublicationView(LoginRequiredMixin, FormView):
    template_name = 'accounts/publications/createNewPublication.html'
    form_class = ChangeProfileForm

    def get_initial(self):
        user = self.request.user
        initial = super().get_initial()
        initial['first_name'] = user.first_name
        initial['last_name'] = user.last_name
        return initial

    def form_valid(self, form):
        user = self.request.user
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.save()

        messages.success(self.request, _('Profile data has been successfully updated.'))

        return redirect('accounts:createNewPublication')

class PublicationsListView(LoginRequiredMixin):
    template_name= 'accounts/publications/publicationList.html'


class LogOutView(LoginRequiredMixin, BaseLogoutView):
    template_name = 'accounts/log_out.html'
