[The Origin] 백엔드 개발자 취업 아카데미 with Django
===
프로젝트 라이언 & 이동원
***

공식문서
- 파이썬 :  https://docs.python.org/
- 장고 : https://docs.djangoproject.com/

# 목차
[1. 개발환경 구성](#1.-개발환경-구성)
 - [Python](#Python)
   - [Python 설치](#python-설치)
 - [VSCode](#VSCode)
   - [VSCode 설치](#vscode-설치)
   - [VSCode 설정](#vscode-설정)

[2. 터미널 명령어](#3.-터미널-명령어)
 - [디렉토리 관련](#디렉토리-관련)
 - 

[3. 장고](#3.-장고)
   - [장고 설치](#장고-설치)
# 1. 개발환경 구성
## Python
### Python 설치
 - 다운로드 URL : https://www.python.org/downloads/
 - 설치 시 유의사항
   - 윈도우 설치 시 <code>'Add Python x.x to PATH'</code> 체크

## VSCode
### VSCode 설치
 - 다운로드 URL : https://code.visualstudio.com/
### VSCode 설정
 - [참고링크](https://code.visualstudio.com/docs/python/tutorial-django)
 - 인터프리터 지정 : <code>VSCode 상단 메뉴바 > View(보기) > Command Palette(Ctrl+Shift+P) > Python: Select Interpreter</code>
 - 확장프로그램(Extensions)
   1. [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
   2. [Korean Language Pack for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-ko)
   3. [indent-rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow)
   4. [vscode-icons](https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons)

# 2. 터미널 명령어
## 디렉토리 관련
```bash
#현재 디렉토리 파일, 디렉토리 확인  
##윈도우
dir

##맥
ls -al

#디렉토리 이동
##윈도우, 맥
cd [디렉토리명]
## 상위 디렉토리 이동
cd ..
```
## 그 밖에
```bash
#터미널 텍스트 삭제
##윈도우
cls

##맥
clear
```
## 파이썬 관련
### 파이썬
윈도우는 <code>python</code>, 맥은 <code>python3</code>를 사용합니다.  
맥은 기본적으로 파이썬2가 설치되어있어 <code>python3</code>를 꼭 붙여주셔야 합니다.
```bash
##윈도우
python
pip

##맥
python3
pip3
```

### 파이썬 패키지 관련
```bash
#패키지 확인
##윈도우
pip list

##맥
pip3 list

#패키지 설치
##윈도우
pip install [패키지명]

##맥
pip3 install [패키지명]

#패키지 제거
##윈도우
pip uninstall [패키지명]

##맥
pip3 uninstall [패키지명]


#패키지 업그레이드
##윈도우
pip install --upgrade pip

##맥
pip3 install --upgrade pip


```

### 가상환경
* 가상환경을 만들 때에는 장고 프로젝트 폴더를 생성하여 디렉토리를 이동한 후 생성해야 함(아래 명령어 입력)
* 가상환경 명은 venv가 아니여도 상관없으나 venv 사용을 권장
```bash
#가상환경 생성
##윈도우
python -m venv venv

##맥
python3 -m venv venv

#가상환경 접속
##윈도우
.\venv\Scripts\activate

##맥
source venv/bin/activate

```

# 3. 장고
## 장고 설치
```bash
##윈도우
pip install django

##맥
pip3 install django
```
## 장고 생성
* 장고 프로젝트 생성 시 프로젝트 명은 제한은 없으나 협업, 유지보수를 위해 <code>config</code>로 하는 것을 권장
* <code>django-admin startproject [장고 프로젝트명] [위치|생략 가능]</code>
  * 위치를 생략할 경우 장고 프로젝트명으로 폴더가 생기면서 생성됨
* 장고 프로젝트, 장고 앱 생성 시 <code>django-admin</code> 명령어 사용
```bash
# 장고 생성
##윈도우, 맥
django-admin startproject confg .
```

## 장고 실행
* 장고 개발서버 실행은 
```bash
#장고 실행
##윈도우
python manage.py runserver

##맥
python3 manage.py runserver
```

# 4. 장고 모델(Models)
* 장고 ORM의 하나의 요소로 데이터베이스를 관리하기 위한 목적
* Models 공식문서 : https://docs.djangoproject.com/en/4.0/topics/db/models/

## DB 관련 명령어
```bash
#마이그레이션 생성
##윈도우
python manage.py makemigration

##맥
python3 manage.py makemigration

#마이그레이트
##윈도우
python manage.py migrate

##맥
python3 manage.py migrate
```

## 모델 필드
### 주요 필드 종류
|   필드명    | 내용              |                비고                 |
|:--------:|:----------------|:---------------------------------:|
|CharField|작거나 큰 문자열을 위한 문자열 필드입니다.||
|TextField|큰 텍스트 필드입니다.||
|IntegerField|정수입니다.| 범위 -2147483648 <br/>~ 2147483647 |
|FloatField|Python에서 float 인스턴스 표현되는 부동 소수점 숫자 입니다.||
|BooleanField| 참/거짓 필드.||
|DateTimeField|Python에서 datetime.datetime 인스턴스 로 표시되는 날짜 및 시간 입니다.||
|FileField| 파일 업로드 필드입니다.||
|ForeignKey| 다대일 관계입니다.||
|ManyToManyField|다대다 관계.||
* 모델 필드 공식문서 : https://docs.djangoproject.com/en/4.0/ref/models/fields/
* 모델 필드 유형 공식문서 : https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types

### 필드 옵션
|  옵션명  | 내용                                                        |비고|
|:-----:|:----------------------------------------------------------|:---------------------------------:|
| null  | 데이터베이스에서와 True같이 빈 값을 저장 합니다.                             ||
| blank | True필드를 공백으로 사용할 수 있습니다.                                  ||
|choices| 이 필드의 선택 항목으로 사용할 정확히 두 항목(예: ) 의 반복 가능 항목으로 구성된 시퀀스 입니다. ||
|default| 필드의 기본값입니다.                                               ||
|editable| False필드가 관리자 또는 기타 항목에 표시되지 않습니다.                         ||
|help_text|양식 위젯과 함께 표시할 추가 "도움말" 텍스트입니다.||
|unique|True이 필드는 테이블 전체에서 고유해야 합니다.||
|validators|이 필드에 대해 실행할 유효성 검사기 목록입니다.||
* 필드 옵션 공식문서 : https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-options

## QuerySet API
### 주요 함수
#### 새로운 QuerySet 반환 메소드
|         함수명         | 내용                                                       |비고|
|:-------------------:|:---------------------------------------------------------|:---------------------------------:|
|filter()| QuerySet주어진 조회 매개변수와 일치 하는 새 포함 개체를 반환합니다 .              ||
|exclude()| 주어진 조회 매개변수와 일치 하지 않는 새 QuerySet포함 개체를 반환합니다.            ||
|annotate()|uerySet제공된 쿼리 표현식 목록으로 의 각 개체에 주석을 답니다 .||
|order_by()|기본적으로 a QuerySet에 의해 반환된 결과 ordering는 모델의 Meta. 메서드 QuerySet를 사용하여 이를 기반으로 재정의할 수 있습니다 .||
|select_related()|QuerySet쿼리를 실행할 때 추가 관련 개체 데이터를 선택하여 외래 키 관계를 "따를" 것을 반환 합니다.||
|prefetch_related()|지정된 QuerySet각 조회에 대한 관련 개체를 단일 일괄 처리에서 자동으로 검색하는 반환합니다.||

#### 새로운 QuerySet 반환 메소드
|         함수명         | 내용                                                       |비고|
|:-------------------:|:---------------------------------------------------------|:---------------------------------:|
|get()|필드 조회 에 설명된 형식이어야 하는 지정된 조회 매개변수와 일치하는 객체를 반환 합니다 .||
|create()|한 번에 개체를 만들고 모두 저장할 수 있는 편리한 방법입니다.||
|bulk_create()|이 메서드는 제공된 객체 목록을 효율적인 방식으로 데이터베이스에 삽입하고(객체가 얼마나 많은지 상관없이 일반적으로 1개의 쿼리만) 생성된 객체를 제공된 것과 동일한 순서로 목록으로 반환합니다.||
|count()|일치하는 데이터베이스의 개체 수를 나타내는 정수를 반환합니다.||
|first()|쿼리 세트와 일치하는 첫 번째 개체를 반환하거나 None일치하는 개체가 없는 경우 반환합니다.||
|aggregate()|집계 값(평균, 합계 등)의 사전을 반환합니다.||
|update()|지정된 필드에 대해 SQL 업데이트 쿼리를 수행하고 일치하는 행 수를 반환합니다.||
|delete()|모든 행에 대해 SQL 삭제 쿼리를 수행하고 삭제 QuerySet된 개체 수와 개체 유형당 삭제 수가 포함된 사전을 반환합니다.||
* QuerySet API 공식문서 : https://docs.djangoproject.com/en/4.0/ref/models/querysets/
