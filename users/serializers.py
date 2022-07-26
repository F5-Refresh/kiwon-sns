import re

from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User


class SignUpSerializer(ModelSerializer):
    def create(self, validated_data):
        password = validated_data.get('password')

        # 비밀번호 8~15자/소문자,숫자 최소하나 사용
        password_re = re.compile('^(?=.{8,15}$)(?=.*[a-z])(?=.*[0-9]).*$')

        if not re.match(password_re, password):
            raise serializers.ValidationError({"password": ["비밀번호는 8~15자의 영소문자와 숫자로 이루어져야 합니다."]})

        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ['email','name', 'password']
        extra_kwargs = {'password': {'write_only': True}}




class SignInSerializer(TokenObtainPairSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def validate(self, data):
        email = data['email']
        password = data['password']

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)

            if not user.check_password(password):
                raise serializers.ValidationError('비밀번호가 다릅니다')
        else:
            raise serializers.ValidationError('일치하는 계정이 없습니다')

        token = RefreshToken.for_user(user)
        refresh = str(token)
        access = str(token.access_token)

        update_last_login(None, user)

        data = {
            'email' : user.email,
            'access' : access,
            'refresh' : refresh
        }

        return data

