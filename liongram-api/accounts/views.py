from django.contrib.auth import authenticate

from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from drf_yasg.utils import swagger_auto_schema

from .serializers import LoginSerializers, TokenSerializers

@api_view(['POST'])
@permission_classes([AllowAny])
@swagger_auto_schema(request_body=LoginSerializers, responses={200: TokenSerializers})
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password,)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response(status=401)

class LoginView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=LoginSerializers, responses={200: TokenSerializers})
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password,)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response(status=401)