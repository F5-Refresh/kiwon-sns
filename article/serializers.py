
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
        print(hashtags_data)        #[OrderedDict([('hashtag', '#harry')]), OrderedDict([('hashtag', '#potter')])]
        article = Article.objects.create(**validated_data)
        print(article)  # user:ddd,title:Harry Potter and the Half-Blood Prince
        print(article.hashtags)     #article.Hashtag.None
        print(article.title)        #title출력
        hts = []
        for tag in hashtags_data:

            # if ht := Hashtag.objects.filter(hashtag=tag['hashtag']):        # #potter
            #     pass
            tag_data = tag['hashtag'][1:]
            print(tag_data)
            pip = Hashtag.objects.filter(hashtag=tag_data)      # db에서 filter로 hashtag 가져오기
            print(pip)

            ht = Hashtag.objects.filter(hashtag=tag_data).first()   # queryset으로 가져왔으니 first함수로 가장 첫번째 row만 조회
            print(ht)


            if ht:  # 값이 존재하면 True /False
                pass
            else:
                print(tag_data)                 # harry
                ht = Hashtag.objects.create(hashtag=tag_data)
                print(ht)
                # ht.save()
            hts.append(ht)
        print(hts)          # [<Hashtag: harry>, <Hashtag: potter>]
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
