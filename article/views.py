
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from article.models import Article
from article.serializers import ArticleCreateSerializer, ArticleListSerializer ,ArticlePatchSerializer


class ArticleCreateUpdateAPIView(APIView):

    def post(self, request):    
        """
        게시글 생성
        """
        data = {'user': request.user.id} | request.data
        # for i in Article.objects.all():   # ordering test
        #     print(i.id)
        # print(request.user.id)      # 1
        # print(data)                 # {'user': 1, 'title': '개발', 'content': '개발스', 'hashtag': '#개발개발'}
        # print(request.data)         # {'title': '개발', 'content': '개발스', 'hashtag': '#개발개발'}
        serializer = ArticleCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def patch(self, request, article_id):
        """
        게시글 수정
        """
        data = {'user': request.user.id} | request.data
        article = get_object_or_404(Article, id=article_id)

        serializer = ArticlePatchSerializer(data=data, instance=article)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['PATCH'])
    def patch_delete(request,article_id):
        """
        delete_flag로 게시글을 삭제하거나 복구할 수 있습니다.
        """
        article = get_object_or_404(Article, id=article_id)
        article.delete_on()
        if article.delete_flag == True: message ="삭제"
        else: message = "복구"
        return Response({"detail":message},status=status.HTTP_200_OK)


class ArticleListAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer



