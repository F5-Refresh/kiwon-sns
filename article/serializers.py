from rest_framework import serializers

from article.models import Article, Hashtag


class HashtagsSerializer(serializers.ModelSerializer):
    """
    해시태그 시리얼라이저
    """
    hashtag = serializers.CharField()

    class Meta:
        model = Hashtag
        fields = ['hashtag']



class ArticleListSerializer(serializers.ModelSerializer):
    """
    게시글 목록 시리얼라이저
    """
    name = serializers.ReadOnlyField(source='user.name')

    total_likes = serializers.SerializerMethodField()
    hashtags = HashtagsSerializer(many=True)

    class Meta:
        model = Article
        fields = ['id','name','title','hashtags','total_likes','view','delete_flag',"created"]

    def get_total_likes(self,instance):
        return instance.likes.count()


class ArticleCreateSerializer(serializers.ModelSerializer):
    """
    게시글 생성 시리얼라이저
    """
    name = serializers.ReadOnlyField(source="user.name")
    hashtags = HashtagsSerializer(many=True)

    class Meta:
        model = Article
        fields = ['name','title','content','hashtags']

    def create(self, validated_data):
        """
        해시태그 생성
        """
        hashtags_data = validated_data.pop('hashtags')
        article = Article.objects.create(**validated_data)
        hts = []
        for tag in hashtags_data:
            tag_data = tag['hashtag'][1:]

            if ht:= Hashtag.objects.filter(hashtag=tag_data).first():
                pass
            else:
                ht = Hashtag.objects.create(hashtag=tag_data)

            hts.append(ht)
        article.hashtags.set(hts)
        return article


class ArticleRetrievePatchSerializer(serializers.ModelSerializer):
    """
    게시글 조회,수정,삭제 시리얼라이저
    """
    name = serializers.ReadOnlyField(source="user.name")
    total_likes = serializers.SerializerMethodField()
    hashtags = HashtagsSerializer(many=True)

    class Meta:
        model = Article
        fields = ['name','title','content','hashtags','total_likes','view','delete_flag','created']

    def get_total_likes(self,instance):
        return instance.likes.count()

    def update(self, article, validated_data):
        article.title = validated_data.get('title', article.title)
        article.content = validated_data.get('content', article.content)
        
        article.hashtags.clear()

        hashtags_data = validated_data.pop('hashtags')
        hts = []
        for tag in hashtags_data:
            tag_data = tag['hashtag'][1:]

            if ht := Hashtag.objects.filter(hashtag=tag_data).first():
                pass
            else:
                ht = Hashtag.objects.create(hashtag=tag_data)
            hts.append(ht)

        article.hashtags.set(hts)
        return article

