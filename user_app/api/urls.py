from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

from user_app.api.views import registration_view, login_view

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('signup/', registration_view, name='registration'),
    path('logout/', login_view, name='logout')
]

