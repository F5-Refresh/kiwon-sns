from rest_framework import serializers

from users.models import User


class SignUpSerializer(serializers.ModelSerializer):
# 입력받은 데이터를 검증
    def create(self, validated_data):
        # create method를 따로 정해준 이유
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ['name', 'password']
        # password는 update,create할 때는 사용되지만, serializing할 때는 포함되지않도록 하기
        extra_kwargs = {'password': {'write_only': True}}