from django.contrib import admin

from article.models import Article, Hashtag


admin.site.register(Hashtag)

class ArticleAdmin(admin.ModelAdmin):
    def user_name(self, obj):
        return obj.user.name

    def get_hashtag(self, obj):
        return ',\n'.join([i.hashtag for i in obj.hashtags.all()])

    list_display = ['title','user_name','get_hashtag']

    search_fields = ['title', 'hashtags__hashtag']

admin.site.register(Article, ArticleAdmin)