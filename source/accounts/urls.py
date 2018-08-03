from django.urls import path

from .views import (LogInView, SignUpView, LogOutView, ChangeProfileView)

app_name = 'accounts'

urlpatterns = [
    path('log-in/', LogInView.as_view(), name='log_in'),
    path('log-out/', LogOutView.as_view(), name='log_out'),    
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('change/profile/', ChangeProfileView.as_view(), name='change_profile')
    #path('list_publication_actives, listPublicationView.as_view(), name='list_publication'),
    #path('add_publication, addpublicationView-as_view(), name='add_publication')
]
