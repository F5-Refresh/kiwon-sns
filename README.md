# SNS 프로젝트 

원티드 프리온보딩에서 진행한 과제, ```SNS 프로젝트``` 입니다.   

<br/>


# 📢서비스 개요
* 본 서비스는 SNS(Social Networking Service) 입니다.   

✔ 유저는 
* 서비스에 접속하여 게시물을 업로드하고 수정, 삭제 및 복구 할 수 있습니다.
* 다른 사람의 게시물을 확인하고, 좋아요를 누를 수 있습니다.
* 원하는 대로 정렬하거나 키워드를 검색할 수 있습니다.

<br/>

# 🔨 Stack
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"> <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white"> <img src="https://img.shields.io/badge/DJANGO_REST_Framework-ff1709?style=for-the-badge&logo=Django&logoColor=white">


<br/>

# 🎫ERD 

![image](https://user-images.githubusercontent.com/87809367/180916546-9bd0d2b2-b9c9-42a2-b04d-42e42e825fe7.png)


<br/>


# 🔑 API docs

| Action | Method | Url | Permission |
| --- | --- | --- | --- |
| 회원가입 | POST | users/signup/ | AllowAny |
| 로그인 | POST | users/signin/ | AllowAny |
| 게시글 리스트 | GET | article/list/ | AllowAny |
| 게시글 작성 | POST | article/ | IsAuthenticated |
| 게시글 상세 | GET | article/<int: article_id> | IsAuthenticated |
| 게시글 수정 | PATCH | article/<int: article_id> | IsAuthenticated |
| 게시글 삭제 및 복구 | PATCH | aritcle/<int: article_id>/delete_on | IsAuthenticated |
| 좋아요 및 좋아요 취소 | PATCH | aritcle/<int: article_id>/like | IsAuthenticated |  

<br/>

# ⚡요구사항 미충족 및 추후 도전 사항  
* 해시태그 입력 시 ','로 구분되는 텍스트가 입력되도록 구현  
* 해시태그 조회 시 #해시태그 형태로 조회되도록 구현
* 해시태그 검색 시, 해시태그를 모두 가진 게시글 목록을 가져오도록 구현  
   예시) ?hastags=서울,맛집 >> “서울" 과 “맛집” 해시태그를 모두 가진 게시글 목록.   
[ex. “서울” 검색 시 > #서울(검색됨) / #서울맛집 (검색안됨)  / #서울,#맛집(검색됨)]  
[ex. “서울,맛집” 검색 시 > #서울(검색안됨) / #서울맛집 (검색안됨)  / #서울,#맛집(검색됨)]   
<br/>

* 댓글 기능 

<br/>

# 🎇구현

> ## 1. 회원가입 
* 유저를 생성합니다.  
* 이메일로 가입 합니다.

</br>

> ## 2. 로그인
* ```JWT 인증방식``` 로그인을 구현하였습니다. (Simple JWT사용)
* 로그아웃은 프론트에서 처리합니다.

</br>

> ## 3. 게시글 생성, 수정, 삭제  

<br/>

✔ 유저는  
* 제목, 내용, 해시태그를 입력하여 게시글을 ```생성```할 수 있습니다.  
    유저는 해당 API 를 요청한 ```인증정보에서 추출```하여 등록 합니다.  
    해시태그는 #으로 시작합니다.  
    아래와 같이 request body에 data를 보냅니다.
    
```json
{
    "title":"toto",
    "content":"tutu",
    "hashtags" : [
                {"hashtag" : "#test1"},
                {"hashtag" : "#test2"}
                ]
}
```

✔ 작성자는,
* 제목, 내용, 해시태그를 ```수정```할 수 있습니다.  
* ```삭제```하고, 삭제한 게시글을 ```복구``` 할 수 있습니다.

</br>

>## 4. 게시글 상세 조회

</br>

✔ 유저는
* 아래와 같이 게시글을 상세 조회할 수 있습니다.  
* 작성자를 포함한 사용자는 본 게시글에 ```좋아요```를 누를 수 있습니다.  
좋아요된 게시물에 다시 좋아요를 누르면 ```취소```됩니다.
* 작성자 포함한 사용자가 게시글을 상세보기 하면 ```조회수가 1``` 증가합니다.  
횟수는 제한이 없습니다.

<br/>

```json
{
    "name": "kiwon",
    "title": "Harry Potter and the Goblet of Fire",
    "content": "hahahahah",
    "hashtags": [
        {
            "hashtag": "harry"
        },
        {
            "hashtag": "potter"
        }
    ],
    "total_likes": 2,
    "view": 5,
    "delete_flag": false,
    "created": "2022-07-22T17:38:28.737932Z"
}
```

<br/>

>## 5. 게시글 목록

<br/>

✔ 유저는  
* 정렬  
```?ordering=total_likes```  
원하는 값으로 게시글 목록을 정렬 할 수 있습니다.  
작성일, 좋아요, 조회수 중 1개를 선택할 수 있습니다.    
default 값은 작성일입니다.  
오름차 순, 내림차 순을 선택할 수 있습니다.

* 검색  
  ```?search=good```  
사용자는 입력한 키워드로 해당 키워드를 포함한 제목을 조회할 수 있습니다.  

* 페이지  
```?limit=5&offset=10```  
사용자는 1페이지 당 게시글 수를 조정할 수 있습니다.  
default값은 10건입니다.  

* 필터링  
```?hashtags=harry```   
사용자는 지정한 키워드로 해당 키워드를 포함한 게시물을 필터링할 수 있습니다.

<br/>

위에서 언급한 4가지 동작은 동시에 적용될 수 있습니다.



