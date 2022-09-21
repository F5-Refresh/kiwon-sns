# 💌 SNS 프로젝트 

원티드 프리온보딩에서 진행한 과제, ```SNS 프로젝트``` 입니다.   

<br/>

> 개발기간 : 7.20 ~ 7.27 ~

> 고도화예정 
* 게시물 테스트 코드 작성
* 로그아웃 redis 
* aws rds -> ok!

<br/>


# 📢서비스 개요
* 본 서비스는 SNS(Social Networking Service) 입니다.   

✔ 유저는 
* 서비스에 접속하여 게시물을 업로드하고 수정, 삭제 및 복구 할 수 있습니다.
* 다른 사람의 게시물을 확인하고, 좋아요를 누를 수 있습니다.
* 원하는 대로 정렬하거나 키워드를 검색할 수 있습니다.

<br/>

# 🔨 Stack
<img src="https://img.shields.io/badge/Python-3766AB?style=flat-square&logo=Python&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Django_REST_framework-ff1709?style=flat-square&logo=Django&logoColor=white"/></a>
<img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=Amazon%20AWS&logoColor=white">
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=Docker&logoColor=white">
<img src="https://img.shields.io/badge/NGINX-009639?style=flat-square&logo=NGINX&logoColor=white">
<img src="https://img.shields.io/badge/Gunicorn-499848?style=flat-square&logo=Gunicorn&logoColor=white">
<img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white">
<img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=SQLite&logoColor=white">

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
좋아요를 ```취소```할 수 있습니다.
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

<br/>

# 🚩 테스트  
* 회원가입 테스트 : 4개  
* 로그인 테스트 : 3개  
* 게시글 테스트 : 3개~ 추가 예정  

<br/>

# 🛫배포
<br/>

```nginx```와 ```gunicorn```을 이용하여 ```aws ec2```서버에서 django 프로젝트를 배포하였습니다.  
db는 로컬에서 개발할 땐 sqlite를 사용하고, 배포할 때는 ```mysql```을 사용하였습니다.  

<br/>

아래에 해당 서버에 접속하여 postman과 웹에서 테스트한 것을 첨부하겠습니다.    
지금은 비용 문제로 서버를 중단했습니다.     

<br/> 

<details>
<summary>로그인</summary>
<div markdown="1">

![image](https://user-images.githubusercontent.com/87809367/182327941-929b7c3f-6905-47b1-bd42-daf9e729a84b.png)

</div>
</details>


<details>
<summary>게시글 생성</summary>
<div markdown="1">

![image](https://user-images.githubusercontent.com/87809367/182330695-f057bd8b-9b87-49c8-8ac9-7ffde32ec423.png)


</div>
</details>

<details>
<summary>게시글 리스트 & 필터링</summary>
<div markdown="1">

<br/>

> 해시태그 키워드 cat을 검색하여 조회수 내림차순으로 정렬한 모습입니다.  

<br/>

![image](https://user-images.githubusercontent.com/87809367/182334343-af08b3a3-b859-4ae5-8d04-6caff23df183.png)

<br/>

> 필터링은 아래와 같이 볼 수 있습니다.  

![image](https://user-images.githubusercontent.com/87809367/182334628-f8e48ead-be5e-4475-a578-bb24933e4363.png)


</details>
















