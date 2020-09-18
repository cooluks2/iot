"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from bookmark.views import BookmarkLV, BookmarkDV
# from bookmark.views import index, detail
from mysite.views import HomeView, UserCreateView, UserCreateDoneTV

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # 로그인, 로그아웃, 비밀번호 변경 등 담당
    path('accounts/', include('django.contrib.auth.urls')),
    # 회원 가입 및 처리
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),


    path('', HomeView.as_view(), name='home'),

    path('admin/', admin.site.urls),
    # class-based views

    # 클래스 기반 뷰
    # path('bookmark/', BookmarkLV.as_view(), name='index'),
    # path('bookmark/<int:pk>', BookmarkDV.as_view(), name='detail'),

    # 함수 기반 뷰
    # path('bookmark/', index, name='index'),
    # path('bookmark/<int:pk>', detail, name='detail'),

    path('bookmark/', include('bookmark.urls')),  # bookmark.urls를 가져오겠다.
    path('blog/', include('blog.urls')),

    # path('tinymce/', include('tinymce.urls')),
]
