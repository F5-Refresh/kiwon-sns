from rest_framework import serializers

from article.models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    """
    게시글 목록 시리얼라이저
    """
    name = serializers.ReadOnlyField(source="user.name")

    class Meta:
        model = Article
        fields = ['name','title','hashtag','like','view','delete_flag',"created"]



class ArticleCreateSerializer(serializers.ModelSerializer):
    """
    게시글 생성 시리얼라이저
    """
    name = serializers.ReadOnlyField(source="user.name")

    class Meta:
        model = Article
        fields = ['user','name','title','content','hashtag']


class ArticlePatchSerializer(serializers.ModelSerializer):
    """
    게시글 수정,삭제 시리얼라이저
    """
    class Meta:
        model = Article
        fields = ['title','content','hashtag','delete_flag']

