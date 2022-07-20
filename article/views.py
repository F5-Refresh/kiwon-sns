
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from article.models import Article
from article.serializers import ArticleCreatePatchSerializer


class ArticleCreateUpdateAPIView(APIView):
    def post(self, request):
        data = {'user': request.user.id} | request.data
        print(request.user.id)      # 1
        print(data)                 # {'user': 1, 'title': '개발', 'content': '개발스', 'hashtag': '#개발개발'}
        print(request.data)         # {'title': '개발', 'content': '개발스', 'hashtag': '#개발개발'}
        serializer = ArticleCreatePatchSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def patch(self, request, article_id):
        data = {'user': request.user.id} | request.data
        article = get_object_or_404(Article, id=article_id)

        serializer = ArticleCreatePatchSerializer(data=data, instance= article)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



