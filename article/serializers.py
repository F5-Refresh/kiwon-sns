
from rest_framework import serializers

from article.models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    """
    게시글 목록 시리얼라이저
    """
    name = serializers.ReadOnlyField(source="user.name")
    total_likes = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id','name','title','hashtag','total_likes','view','delete_flag',"created"]

    def get_total_likes(self,instance):
        return instance.likes.count()


class ArticleCreateSerializer(serializers.ModelSerializer):
    """
    게시글 생성 시리얼라이저
    """
    name = serializers.ReadOnlyField(source="user.name")

    class Meta:
        model = Article
        fields = ['user','name','title','content','hashtag']


class ArticleRetrievePatchSerializer(serializers.ModelSerializer):
    """
    게시글 조회,수정,삭제 시리얼라이저
    """
    name = serializers.ReadOnlyField(source="user.name")
    total_likes = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['name','title','content','hashtag','likes','view','delete_flag','created']
        read_only_fields = ['likes','view','delete_flag','created']

    def get_total_likes(self,instance):
        return instance.likes.count()
