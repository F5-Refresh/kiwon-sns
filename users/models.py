from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models

from core.models import AbstractTimeStamp


class UserManager(BaseUserManager):
# 유저 생성
    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user
# 관리자 유저
    def create_superuser(self,email,name, password):
        user = self.create_user(
            email, password=password, name=name
        )
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,AbstractTimeStamp):
    email = models.EmailField(verbose_name="이메일",max_length=300,unique=True,blank=False)
    name = models.CharField(verbose_name="작성자",max_length=300,unique=True,blank=False)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f"{self.pk},{self.email}, {self.name}"

    # 권한 설정
    def has_perm(self, perm, obj=None):
        return True

    # app, model 접근가능
    def has_module_perms(self, app_label):
        return True

    # 장고관리자 화면에 로그인
    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = 'users'