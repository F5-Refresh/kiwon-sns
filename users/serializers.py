from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User


class SignUpSerializer(ModelSerializer):
    #회원가입

# 입력받은 데이터를 검증
    def create(self, validated_data):
        # create method를 따로 정해준 이유
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ['email','name', 'password']       #수정햇슴
        # password는 update,create할 때는 사용되지만, serializing할 때는 포함되지 않도록 하기
        extra_kwargs = {'password': {'write_only': True}}




class SignInSerializer(TokenObtainPairSerializer):
    # 로그인

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

