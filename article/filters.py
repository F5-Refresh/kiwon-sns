import django_filters

from article.models import Article
from django_filters import rest_framework as filters



class HashtagFilter(filters.FilterSet):
    """
    해시태그를 필터링합니다.
    """
    hashtags = django_filters.CharFilter(method='filter_hashtags')

    def filter_hashtags(self, queryset, name, value):       # name = hashtags
        lookup = '__'.join([name, 'hashtag'])               # name__hashtag -> hashtags__hashtag
        return queryset.filter(**{lookup: value})

    class Meta:
        model = Article
        fields = ['hashtags']


















