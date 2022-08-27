
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import SignUpSerializer, SignInSerializer


class SignUpView(APIView):
    permission_classes = [AllowAny,]

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '회원가입이 완료 되었습니다.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignInView(APIView):
    permission_classes = [AllowAny,]

    def post(self, request):
        serializer = SignInSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):

            token = serializer.validated_data
            return Response(token,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

