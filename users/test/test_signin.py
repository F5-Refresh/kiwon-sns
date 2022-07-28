# from rest_framework.test import APIClient, APITestCase
# from rest_framework import status
# from users.models import User

# class SignInJWTTest(APITestCase):
#     """
#     JWT 로그인 테스트
#     """
#     client = APIClient()
    
#     @classmethod
#     def setUpTestData(cls):
#         """
#         회원을 셋업합니다.
#         """
#         cls.user = User.objects.create_user(
#             email = 'test@example.com',password='test1234', name = 'tester')
    
    
#     def test_login_jwt(self):
#         """
#         로그인 성공 테스트입니다.
#         access token을 받아 로그인에 성공한 뒤 
#         로그인을 한 사용자만 접근할 수 있는 페이지에 접속할 수 있는지 확인합니다.
#         """
#         url = '/users/signin/'
#         response = self.client.post(url,{'email':'test@example.com', 'password':'test1234'}, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertTrue('access' in response.data)
#         self.assertTrue('refresh' in response.data)
        
#         token = response.data['access']
#         client = APIClient()
#         client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
#         res = client.get('/article/1', data={'format':'json'})
#         self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
        
        
#     def test_fail_signin_with_wrong_email(self):
#         """
#         잘못된 이메일로 로그인을 하는 실패테스트입니다.
#         """
#         url = '/users/signin/'
#         response = self.client.post(url,{'email':'wrong@example.com', 'password':'test1234'}, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


#     def test_fail_signin_with_wrong_password(self):
#         """
#         잘못된 비밀번호로 로그인을 하는 실패테스트입니다.
#         """
#         url = '/users/signin/'
#         response = self.client.post(url,{'email':'test@example.com', 'password':'wrong1234'}, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
