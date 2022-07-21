from django.urls import path

from article.views import ArticleAPIView, ArticleListAPIView

urlpatterns =[
    path('', ArticleAPIView.as_view(), name ='article'),
    path('<int:article_id>',ArticleAPIView.as_view(), name ='article'),
    path('<int:article_id>/delete_on', ArticleAPIView.patch_delete),
    path('list',ArticleListAPIView.as_view())
]



