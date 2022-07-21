from django.urls import path

from article.views import ArticleCreateUpdateAPIView, ArticleListAPIView

urlpatterns =[
    path('', ArticleCreateUpdateAPIView.as_view(), name ='article'),
    path('<int:article_id>',ArticleCreateUpdateAPIView.as_view(),name ='article'),
    path('<int:article_id>/delete_on', ArticleCreateUpdateAPIView.patch_delete),
    path('list',ArticleListAPIView.as_view())
]



