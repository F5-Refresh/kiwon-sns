from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics, filters
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Sum

from article.filters import HashtagFilter
from article.models import Article
from article.serializers import ArticleCreateSerializer, ArticleListSerializer, ArticleRetrievePatchSerializer


class ArticleAPIView(APIView):

    def get(self, request ,article_id):
        """
        게시글 상세페이지를 조회합니다.
        조회를 할 때마다 조회수는 1씩 증가합니다.
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
        serializer = ArticleCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, article_id):
        """
        게시글을 수정합니다.
        """
        article = get_object_or_404(Article, id=article_id, user=request.user.id)
        serializer = ArticleRetrievePatchSerializer(data=request.data, instance=article, partial=True)

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


class ArticleListAPIView(generics.ListAPIView):
    """
    게시글 리스트를 조회합니다.
    """
    permission_classes = [AllowAny,]
    queryset = Article.objects.annotate(total_likes=Sum('likes'))
    serializer_class = ArticleListSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]

    # 정렬
    ordering_fields = ['created', 'total_likes', 'view']
    ordering = ['created']

    # 검색
    search_fields = ['title']

    # 해시태그 필터링
    filterset_class = HashtagFilter



