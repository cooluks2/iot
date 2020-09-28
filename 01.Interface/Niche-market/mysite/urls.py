"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from mysite.views import HomeView, UserCreateView, UserCreateDoneTV
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('market/', include('market.urls')),
    path('board/', include('board.urls')),
    path('notice/', include('notice.urls')),
    # 로그인, 로그아웃, 비밀번호 변경 등 담당
    path('accounts/', include('django.contrib.auth.urls')),
    # 회원 가입 및 처리
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(),name='register_done'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
