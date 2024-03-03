from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from user_app.api.serializers import RegistrationSerializers


@api_view(['POST'])
def logout(request):
    if request.method == 'POST' and request.user.is_authenticated():

        Token.objects.get(user=request.user).delete()
        return Response(status=status.HTTP_200_OK, data={'message': 'successfully logged out'})


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):

    if request.method == 'POST':
        serializer = RegistrationSerializers(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = "Registration Successful!"
            data['username'] = account.username
            data['email'] = account.email

            token = Token.objects.get(user=account).key
            data['token'] = token

            # refresh = RefreshToken.for_user(account)
            # data['token'] = {
            #                     'refresh': str(refresh),
            #                     'access': str(refresh.access_token),
            #                 }

        else:
            data = serializer.errors

        return Response(data, status=status.HTTP_201_CREATED)