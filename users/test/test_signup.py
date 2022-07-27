import json

from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from users.models import User

class SignUpTest(APITestCase):
    """
    회원가입 테스트
    """
    client = APIClient()

    @classmethod
    def setUpTestData(cls):
        """
        이미 있는 회원을 셋업합니다.
        """
        cls.user = User.objects.create_user(
            email = 'test@example.com',password='test1357', name = 'tester')

    def test_create_signup(self):
        """
        회원가입 성공 테스트입니다.
        """
        url = '/users/signup/'
        data = {'email': 'chacha@gmail.com', 'password': 'chacha1234', 'name': 'chachacha'}
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {"message": "회원가입이 완료 되었습니다."})
        self.assertEqual(User.objects.filter(email='chacha@gmail.com').exists(), True)

    def test_fail_create_signup_with_wrong_password(self):
        """
        비밀번호를 잘못 구성한 실패 테스트입니다.
        """
        url = '/users/signup/'
        data = {'email': 'hoho@gmail.com', 'password': 'hoho', 'name': 'hohoho'}
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'password': ["비밀번호는 8~15자의 영소문자와 숫자로 이루어져야 합니다."]})

    def test_fail_create_signup_with_existed_account(self):
        """
        이미 있는 email로 가입을 시도한 실패 테스트입니다.
        """
        url = '/users/signup/'
        data = {'email':'test@example.com','password': 'test1234', 'name' : 'heyhey'}

        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'email': ['user with this 이메일 already exists.']})

    def test_fail_create_signup_with_existed_name(self):
        """
        이미 있는 이름으로 가입을 시도한 실패 테스트입니다.
        """
        url = '/users/signup/'
        data = {'email': 'hey@gmail.com', 'password': 'test2222', 'name': 'tester'}

        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'name': ['user with this 작성자 already exists.']})