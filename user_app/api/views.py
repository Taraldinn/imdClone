from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from user_app.api.serializers import RegistartionSerializers


@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistartionSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)