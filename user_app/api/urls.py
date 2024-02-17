from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

from user_app.api.views import registration_view, login_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView



urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('login/', obtain_auth_token, name='login'),
    path('signup/', registration_view, name='registration'),
    path('logout/', login_view, name='logout')
]

