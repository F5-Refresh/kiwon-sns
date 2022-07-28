import json
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from .models import Article, User, Hashtag
from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory
from  article.serializers import ArticleCreateSerializer

class ArticleTest(APITestCase):
    """
    게시글을 생성,수정,삭제를 테스트합니다.
    """
    client = APIClient()
    
    def setUp(self):
        """
        회원을 셋업합니다.
        """
        
        self.user = User.objects.create_user(
            email = 'test@example.com', password='test1234', name = 'tester')
        
        hashtag = Hashtag.objects.create(hashtag='BTS')
        hashtag2 = Hashtag.objects.create(hashtag='#MEENOI')
        hashtag3 = Hashtag.objects.create(hashtag='#VAUNDY')
        print(hashtag)      # #BTS
        
        article = Article.objects.create(user=self.user, title='music', content='is my life')

        print(article.id)
        print(hashtag.id)
        # print(self.article)
        # test = self.article.create(hashtag='#dd')
        # print(test)
        # new_article = self.article.hashtags.create(hashtag='#thth')
        
        # print(f'new_article : {new_article}, {self.article}')
        
        article.hashtags.add(hashtag)
        # article.refresh_from_db
        article.save()
        
        a = ArticleCreateSerializer(article)
        a.is_valid(raise_exception=True)
        
        b = a.save()
        print(b)
        
        # print(a.data.hashtags)
        # print(hashtag.articles)
        # print(self.article)
        # print(self.hashtag.hashtag)
        # hashtag_id = self.hashtag.id
        # # hash_list = [{'hashtag' : cls.hashtag.hashtag, 'id': cls.hashtag.id}]     
        
        # print(self.article)
        # print(self.article.hashtags)
        # self.article.hashtags.set(hashtag_id)
        # print(self.article)
        
        # self.article.set(hashtag2)
        # print(self.article.hashtags)
        # Article.objects.create(user=self.user, title='music2', content='hahah')
        

        
    def test_create_article(self):
        """
        게시글 생성 성공테스트입니다.
        """
        user = User.objects.get(email='test@example.com')
        client = APIClient()
        client.force_authenticate(user=user)
        
        url = '/article/'
        data = {
                'title':'toto',
                'content':'tutu',
                'hashtags' : [
                            {'hashtag' : '#test1'},
                            {'hashtag' : '#test2'}
                            ]
                }
        res = json.dumps(data)
        response = client.post(url, res, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_update_article(self):
    #     """
    #     게시글 업데이트 성공테스트 입니다.
    #     """
    #     user = User.objects.get(email='test@example.com')
    #     client = APIClient()
    #     client.force_authenticate(user=user)
