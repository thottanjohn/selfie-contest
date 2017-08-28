import django

from django.conf.urls import url
from django.conf.urls import include
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import views as auth_views

from django.views.generic.base import TemplateView

from .views import ActivationView
from .views import RegistrationView
from .views import ResendActivationView

app_name="register"
urlpatterns = [
        url(r'^login/$',
            auth_views.LoginView.as_view(
                template_name='registration/login.html'),
            name='auth_login'),
        url(r'^logout/$',
            auth_views.LogoutView.as_view(
                template_name='registration/logout.html'),
            name='auth_logout'),
        url(r'^password/change/$',
            auth_views.PasswordChangeView.as_view(
                success_url=reverse_lazy('register:auth_password_change_done')),
            name='auth_password_change'),
        url(r'^password/change/done/$',
            auth_views.PasswordChangeDoneView.as_view(),
            name='auth_password_change_done'),
        url(r'^password/reset/$',
            auth_views.PasswordResetView.as_view(
                success_url=reverse_lazy('register:auth_password_reset_done')),
            name='auth_password_reset'),
        url(r'^password/reset/complete/$',
            auth_views.PasswordResetCompleteView.as_view(),
            name='auth_password_reset_complete'),
        url(r'^password/reset/done/$',
            auth_views.PasswordResetDoneView.as_view(),
            name='auth_password_reset_done'),
        url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
            auth_views.PasswordResetConfirmView.as_view(
                success_url=reverse_lazy('register:auth_password_reset_complete')),
            name='auth_password_reset_confirm'),
        url(r'^activate/complete/$',
            TemplateView.as_view(template_name='registration/activation_complete.html'),
            name='registration_activation_complete'),
        url(r'^activate/resend/$',
            ResendActivationView.as_view(),
            name='registration_resend_activation'),
        # Activation keys get matched by \w+ instead of the more specific
        # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
        # that way it can return a sensible "invalid key" message instead of a
        # confusing 404.
        url(r'^activate/(?P<activation_key>\w+)/$',
            ActivationView.as_view(),
            name='registration_activate'),
        url(r'^register/complete/$',
            TemplateView.as_view(template_name='registration/registration_complete.html'),
            name='registration_complete'),
        url(r'^register/closed/$',
            TemplateView.as_view(template_name='registration/registration_closed.html'),
            name='registration_disallowed'),
    ]
    
if getattr(settings, 'INCLUDE_REGISTER_URL', True):
    urlpatterns += [
        url(r'^register/$',
            RegistrationView.as_view(),
            name='registration_register'),
    ]