# 실전 프로그램 개발 - 콘텐츠 편집 기능 - (Bookmark)

<br>

### 애플리케이션 설계하기

**모델 설계**

-   Bookmark 모델 클래스

![image-20201006232246538](09_실전_프로그램_개발-콘텐츠_편집_기능(Bookmark).assets/image-20201006232246538.png)  

<br>

**Bookmark URL 설계**

![image-20201006232310292](09_실전_프로그램_개발-콘텐츠_편집_기능(Bookmark).assets/image-20201006232310292.png)  

<br>

### 개발 코딩하기

**bookmark/models.py**

```python
from django.db import models
from django.contrib.auth.models import User

class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=100, blank=True)
    url = models.URLField('URL', unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.title
```

>   `on_delete=models.CASCADE` : 부모 삭제 될 때 자식의 행도 삭제  
>
>   ☆☆☆`owner` 외래키 설정

<br>

**데이터베이스 반영**

$ `python manage.py makemigrations bookmark`

$ `python manage.py migrate`

<br>

**접근 권한 제어 뷰 클래스**

-   django.contrib.auth.mixins.LoginRequiredMixin
    -   로그인 사용자만 뷰가 작동하도록 함
    -   로그인 하지 않고 해당 url로 직접 접근하면 로그인 페이지로 리다이렉트 됨
-   OwnerOnlyMixin
    -   django.contrib.auth.mixins.AccessMixin를 상속
    -   로그인 사용자가 모델 인스턴스의 소유자인 경우에만 뷰가 작동하도록 함

<br>

**mysite/views.py**

```python
:
from django.contrib.auth.mixins import AccessMixin
from django.views.defaults import permission_denied
:
    
class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/delete the object"
    def get(self, request, *args, **kwargs):
        self.object = self.get_object() # 모델 인스턴스 얻기
        if self.request.user != self.object.owner:
            self.handle_no_permission()
        return super().get(request, *args, **kwargs)
```

>   `def get()` : 페이지 요청하는 get이 왔을 때 작동(update, delete)

<br>

**bookmark/views.py**

```python
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin

:
    
class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title', 'url'] # 폼 모델에 사용할 필드  폼 모델 자동 생성
    success_url = reverse_lazy('bookmark:index')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form) 
    
class BookmarkChangeLV(LoginRequiredMixin, ListView):
    template_name = 'bookmark/bookmark_change_list.html'
    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)
    
class BookmarkUpdateView(OwnerOnlyMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'url'] # 폼 모델에 사용할 필드  폼 모델 자동 생성
    success_url = reverse_lazy('bookmark:index')
    
class BookmarkDeleteView(OwnerOnlyMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')
```

>   `owner=self.request.user` : 사용자가 만든 북마크만 제공하기 위함
>
>   `OwnerOnlyMixin` : 자시이 만든 bookmark인지 확인

<br>

**bookmark/urls.py**

```python
from django.urls import path
from bookmark.views import *

app_name = 'bookmark'
urlpatterns = [
    :
    # Example: /bookmark/add/
    path('add/', BookmarkCreateView.as_view(), name="add"),
    # Example: /bookmark/change/
    path('change/', BookmarkChangeLV.as_view(), name="change"),
    # Example: /bookmark/99/update/
    path('<int:pk>/update/', BookmarkUpdateView.as_view(), name="update"),
    # Example: /bookmark/99/delete/
    path('<int:pk>/delete/', BookmarkDeleteView.as_view(), name="delete"),
]
```

<br>

**쓰기 / 수정목록 인터페이스**

![image-20201006233251420](09_실전_프로그램_개발-콘텐츠_편집_기능(Bookmark).assets/image-20201006233251420.png)  

<br>

**bookmark/templastes/bookmark/bookmark_list.html**

```html
:
<div>
    {% if user.is_active %}
    <a href="{%url 'bookmark:add' %}" class="btn btn-primary btn-sm">
        <i class="fas fa-pencil-alt"></i> 쓰기</a>
    
    <a href="{% url 'bookmark:change'%}"
       class="btn btn-primary btn-sm"><i class="far fa-edit"></i> 수정 목록</a>
    {% endif %}
</div>
{% endblock %}
```

<br>

### 개발 코딩하기(쓰기/수정)

**북마크 쓰기/수정**

![image-20201006233351813](09_실전_프로그램_개발-콘텐츠_편집_기능(Bookmark).assets/image-20201006233351813.png)  

<br>

**bookmark/templastes/bookmark/bookmark_form.html**

```html
{% extends "base.html" %}
{% load widget_tweaks %}

{% block title %}bookmark_form.html{% endblock %}

{% block content %}

<h1>Bookmark Create/Update - {{user}}</h1>
<p class="font-italic">This is a creation or update form for your
    bookmark.</p>

{% if form.errors %}
<div class="alert alert-danger">
    <div class="font-weight-bold">
        Wrong! Please correct the error(s) below.</div>
    {{ form.errors }}
</div>
{% endif %}

<form action="." method="post" class="card pt-3">{% csrf_token %}
    <div class="form-group row">
        {{ form.title|
        add_label_class:"col-form-label col-sm-2 ml-3 font-weight-bold" }}
        <div class="col-sm-5">
            {{ form.title|add_class:"form-control"|attr:"autofocus" }}
        </div>
    </div>
    <div class="form-group row">
        {{ form.url|
        add_label_class:"col-form-label col-sm-2 ml-3 font-weight-bold" }}
        <div class="col-sm-5">
            {{ form.url|add_class:"form-control" }}
        </div>
    </div>
    <div class="form-group">
        <div class="offset-sm-2 col-sm-5">
            <input type="submit" value="Submit" class="btn btn-info"/>
        </div>
    </div>
</form>
{% endblock %}
```

<br>

**수정목록**

![image-20201006233511360](09_실전_프로그램_개발-콘텐츠_편집_기능(Bookmark).assets/image-20201006233511360.png)  

>   자신만 들어올 수 있게

<br>

**bookmark/templastes/bookmark/bookmark_change_list.html**

```html
{% extends "base.html" %}
{% block title %}bookmark_change_list.html{% endblock %}
{% block content %}
<h1>Bookmark Change - {{user}}</h1>
<br>
<table class="table table-bordered table-condensed table-striped">
    <thead>
        <tr class="table-primary">
            <th>Title</th>
            <th>Url</th>
            <th>Owner</th>
            <th>Update</th>
            <th>Delete</th>
        </tr>
    </thead>
    <tbody>
        {% for item in object_list %}
        <tr>
            <td>{{ item.title }}</td>
            <td>{{ item.url }}</td>
            <td>{{ item.owner }}</td>
            <td><a href="{% url 'bookmark:update' item.id %}">
                <i class="far fa-edit"></i> 수정</a>
            </td>
            <td><a href="{% url 'bookmark:delete' item.id %}" >
                <i class="fas fa-trash"></i> 삭제</a>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endblock %}
```

<br>

### 개발 코딩하기(삭제)

**삭제 확인 인터페이스**

![image-20201006233643092](09_실전_프로그램_개발-콘텐츠_편집_기능(Bookmark).assets/image-20201006233643092.png)  

<br>

**bookmark/templastes/bookmark/bookmark_confirm_delete.html**

```html
{% extends "base.html" %}
{% block title %}bookmark_confirm_delete.html{% endblock %}

{% block content %}

<h1>Bookmark Delete</h1>
<br>
<form action="." method="post">{% csrf_token %}
    <p>Are you sure you want to delete "{{ object }}" ?</p>
    <input type="submit" value="Confirm" class="btn btn-danger btn-sm" />
</form>
</div>
{% endblock %}
```

<br>

