from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user_app.api.views import signup, logout

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('login/', obtain_auth_token, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout')
]
