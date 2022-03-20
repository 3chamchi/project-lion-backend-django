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