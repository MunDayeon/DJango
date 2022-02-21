"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import firstapp.views   #firstapp 의 views.py 불러와주기

# http://127.0.0.1:8000/ 뒤에 붙는 것이 path('')의 소괄호 안에 들어감
# 어떤 url에 요청이 들어왔을때 views.py에 정의된 함수 중에 어떤 함수를 실행시켜 view에 보여줄지 결정해주는 페이지
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', firstapp.views.home, name='hello_world_page'),  #firstapp의 views.py 파일 안의 home이라는 함수를 실행시켜라
    path('test.html/', firstapp.views.test, name='test_page'),
]
