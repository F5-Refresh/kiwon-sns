from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes

from article.models import Article
from article.serializers import ArticleCreateSerializer, ArticleListSerializer, ArticleRetrievePatchSerializer


class ArticleAPIView(APIView):

    def get(self, request ,article_id):
        """
        게시글 상세페이지를 조회합니다.
        """
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleRetrievePatchSerializer(article)
        article.view += 1
        article.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):    
        """
        게시글 생성합니다.
        """
        data = {'user': request.user.id} | request.data
        serializer = ArticleCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, article_id):
        """
        게시글을 수정합니다.
        """
        data = {'user': request.user.id} | request.data
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleRetrievePatchSerializer(data=data, instance=article, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['PATCH'],)
    def patch_delete(request, article_id):
        """
        delete_flag로 게시글을 삭제하거나 복구할 수 있습니다.
        """
        article = get_object_or_404(Article, id=article_id, user=request.user.id)
        article.delete_on()
        if article.delete_flag == True: message ="삭제"
        else: message = "복구"
        return Response({"detail":message},status=status.HTTP_200_OK)


    @api_view(['PATCH'],)
    def patch_likes(request,article_id):
        """
        좋아요를 누르거나 취소할 수 있습니다.
        """
        article = get_object_or_404(Article, id=article_id)
        if not request.user in article.likes.all():
            article.likes.add(request.user)
            return Response({"detail":"좋아요를 눌렀습니다"}, status=status.HTTP_200_OK)
        else:
            article.likes.remove(request.user)
            return Response({"detail":"좋아요가 취소되었습니다"}, status=status.HTTP_200_OK)


    # @api_view(['PATCH'],)
    # def count_views(request, article_id):
    #     """
    #     조회수를 증가시킵니다.
    #     """
    #     article = Article.objects.get(id=article_id)
    #     article.views =+ 1
    #     article.save()
#
# class ArticleDetailAPIView(APIView):
#
#     permission_classes = [AllowAny, ]
#
#     def get(self, request ,article_id):
#         """
#         게시글 상세페이지를 조회합니다.
#         """
#         article = get_object_or_404(Article, id=article_id)
#         serializer = ArticleRetrievePatchSerializer(article)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request, article_id):
#         """
#         조회수를 증가시킵니다.
#         """
#         article = Article.objects.get(id=article_id)
#         article.view += 1
#         article.save()
#         return

class ArticleListAPIView(generics.ListAPIView):
    """
    게시글 리스트를 조회합니다.
    """
    permission_classes = [AllowAny,]

    queryset = Article.objects.filter(delete_flag=False)
    serializer_class = ArticleListSerializer



