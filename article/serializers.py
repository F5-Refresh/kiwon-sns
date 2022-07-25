
from rest_framework import serializers

from article.models import Article, Hashtag


class HashtagsSerializer(serializers.ModelSerializer):
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
        fields = ['user','name','title','content','hashtags']

    def create(self, validated_data):
        hashtags_data = validated_data.pop('hashtags')
        print(hashtags_data)        # [OrderedDict([('hashtag', '#harry')]), OrderedDict([('hashtag', '#potter')])]
        article = Article.objects.create(**validated_data)
        print(article)  # user:ddd,title:Harry Potter and the Half-Blood Prince

        hts = []
        for tag in hashtags_data:
            if ht := Hashtag.objects.filter(hashtag=tag['hashtag']).first():
                pass
            else:
                tag_data =tag['hashtag'][1:]
                ht = Hashtag.objects.create(hashtag=tag_data)

                ht.save()
            hts.append(ht)
        print(hts)          # [<Hashtag: #harry>, <Hashtag: #potter>]
        print(hts )
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
        read_only_fields = ['total_likes','view','delete_flag','created']

    def get_total_likes(self,instance):
        return instance.likes.count()
