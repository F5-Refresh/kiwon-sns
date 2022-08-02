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
            email = 'test@example.com', password='test1234', name ='tester')
        
        self.article = Article.objects.create(user=self.user, title='music', content='is my life')

        hashtag = Hashtag.objects.create(hashtag='#BTS')
        hashtag2 = Hashtag.objects.create(hashtag='#MEENOI')
        
        self.article.hashtags.set([hashtag, hashtag2])
        
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

    def test_update_article(self):
        """
        게시글 업데이트 성공테스트 입니다.
        """
        user = User.objects.get(email='test@example.com')
        client = APIClient()
        client.force_authenticate(user=user)
        url = '/article/1'
        data = {
                'title':'update test',
                'content':'update',
                'hashtags' : [
                            {'hashtag' : '#check'},
                            {'hashtag' : '#chak'}
                            ]
                }
        res = json.dumps(data)
        response = client.patch(url, res, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
         
    def test_delete_article(self):
        user = User.objects.get(email='test@example.com')
        client = APIClient()
        client.force_authenticate(user=user)

        url = '/article/1/delete_on'
        response = client.patch(url, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    

