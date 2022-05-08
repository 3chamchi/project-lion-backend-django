from rest_framework import serializers

from rest_framework.authtoken.models import Token

class LoginSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class TokenSerializers(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key', ]