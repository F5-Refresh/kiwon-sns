from rest_framework import serializers

from article.models import Article


# class ArticleListSerializer(serializers.ModelSerializer):
#     email = serializers.ReadOnlyField(source="user.email")
#
#     class Meta:
#         model = Article
#         fields = ['email','title','hashtag','like','view']
#


class ArticleCreatePatchSerializer(serializers.ModelSerializer):
    """
    게시글 생성, 수정
    """
    name = serializers.ReadOnlyField(source="user.name")

    class Meta:
        model = Article
        fields = ['user','name','title','content','hashtag']




