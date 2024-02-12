from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view

from user_app.api.serializers import RegistartionSerializers
from user_app.models import create_auth_token



@api_view(['POST'])
def login_view(request):
    if request.method =='POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK, data={'message': 'successfully logged out'})

@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistartionSerializers(data=request.data)

        data = {}

        if serializer.is_valid():

            account = serializer.save()
            data['response'] = 'successfully registered new user.'
            data['username'] = account.username
            data['email'] = account.email
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
