# 실전 프로그램 개발 - 콘텐츠 편집 기능 - (Blog)

<br>

### 애플리케이션 설계하기

**모델 설계**

-   Post 모델 클래스

![image-20201007093534495](10_실전_프로그램_개발-콘텐츠_편집_기능(Blog).assets/image-20201007093534495.png)  

<br>

**Blog URL 설계**

![image-20201007093551433](10_실전_프로그램_개발-콘텐츠_편집_기능(Blog).assets/image-20201007093551433.png)  

<br>

**작업 순서**

![image-20201007093608997](10_실전_프로그램_개발-콘텐츠_편집_기능(Blog).assets/image-20201007093608997.png)  

<br>

### 개발 코딩하기

**blog/models.py**

```python
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True,
                            help_text='one word for title alias.')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
    tags = TaggableManager(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)
    
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_posts'
        ordering = ('-modify_dt',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))
    
    def get_previous(self):
        return self.get_previous_by_modify_dt()
    
    def get_next(self):
        return self.get_next_by_modify_dt()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
```

>   `allow_unicode=True` : save 직전 slug 만든다.

<br>

**데이터베이스 반영**

$ `python manage.py makemigrations blog`

$ `python manage.py migrate`

>   이후 Heidi에서 blog_posts > owner_id에 배정

<br>

**blog/views.py**

```python
:
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin
:
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'description', 'content', 'tags']
    initial = {'slug': 'auto-filling-do-not-input'}
    success_url = reverse_lazy('blog:index')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class PostUpdateView(OwnerOnlyMixin, UpdateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content', 'tags']
    success_url = reverse_lazy('blog:index')
    
class PostDeleteView(OwnerOnlyMixin, DeleteView) :
    model = Post
    success_url = reverse_lazy('blog:index')
```

>   `initial = {'slug': 'auto-filling-do-not-input'}` 
>
>   : 초기값을 담고 있는 사전, key는 fields의 요소

<br>

**blog/urls.py**

```python
from django.urls import path, re_path
from blog.views import *

app_name = 'blog'
urlpatterns = [
    :
    # Example: /blog/add/
    path('add/', PostCreateView.as_view(), name="add"),
    # Example: /blog/99/update/
    path('<int:pk>/update/', PostUpdateView.as_view(), name="update"),
    # Example: /blog/99/delete/
    path('<int:pk>/delete/', PostDeleteView.as_view(), name="delete"),
]
```

<br>

**템플릿**

![image-20201007094759215](10_실전_프로그램_개발-콘텐츠_편집_기능(Blog).assets/image-20201007094759215.png)  

<br>

**글 쓰기 인터페이스**

![image-20201007094813999](10_실전_프로그램_개발-콘텐츠_편집_기능(Blog).assets/image-20201007094813999.png)  

<br>

**blog/templates/blog/post_all.html**

```html
:
    {% include "pagination.html" %}
    {% if user.is_active %}
    <div class="text-right mr-3">
        <a href="{%url 'blog:add' %}" class="btn btn-primary btn-sm">
            <i class="fas fa-pencil-alt"></i> 쓰기</a>
    </div>
    {% endif %}
{% endblock %}
```

<br>

**글 쓰기/수정 화면**

![image-20201007094902802](10_실전_프로그램_개발-콘텐츠_편집_기능(Blog).assets/image-20201007094902802.png)  

<br>

**blog/templates/blog/post_form.html**

```html
{% extends "base.html" %}
{% load widget_tweaks %}

{% block title %}post_form.html{% endblock %}

{% block content %}
<h1>Post Create/Update - {{user}}</h1>
<p class="font-italic">This is a creation or update form for your post.</p>
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
        {{ form.slug|
        add_label_class:"col-form-label col-sm-2 ml-3 font-weight-bold" }}
        <div class="col-sm-5">
            {{ form.slug|add_class:"form-control"|attr:"readonly" }}
        </div>
        <small class="form-text text-muted">{{ form.slug.help_text }}</small>
    </div>
    <div class="form-group row">
        {{ form.description|
        add_label_class:"col-form-label col-sm-2 ml-3 font-weight-bold" }}
        <div class="col-sm-5">
            {{ form.description|add_class:"form-control" }}
        </div>
        <small class="form-text text-muted">
            {{ form.description.help_text }}</small>
    </div>
    <div class="form-group row">
        {{ form.content|
        add_label_class:"col-form-label col-sm-2 ml-3 font-weight-bold" }}
        <div class="col-sm-8">
            {{ form.content|add_class:"form-control" }}
        </div>
    </div>
    <div class="form-group row">
        {{ form.tags|
        add_label_class:"col-form-label col-sm-2 ml-3 font-weight-bold" }}
        <div class="col-sm-5">
            {{ form.tags|add_class:"form-control" }}
        </div>
        <small class="form-text text-muted">{{ form.tags.help_text }}</small>
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

**글 수정/삭제 인터페이스**

![image-20201007095022598](10_실전_프로그램_개발-콘텐츠_편집_기능(Blog).assets/image-20201007095022598.png)  

<br>

**blog/templates/blog/post_detail.html**

```html
:
    <div class="text-right">
        <a href="{% url 'blog:update' post.id %}" class="mr-3">
            <i class="far fa-edit"></i> 수정</a>
        <a href="{% url 'blog:delete' post.id %}" class="text-danger mr-3">
            <i class="fas fa-trash"></i> 삭제</a>
    </div>
    <div>
        {{ post.content|linebreaks }}
    </div>
:
```

>   update view  슬러그 제거

<br>

**글 삭제**

![image-20201007095130625](10_실전_프로그램_개발-콘텐츠_편집_기능(Blog).assets/image-20201007095130625.png)  

<br>

**blog/temaplates/blog/post_confirm_delete.html**

```html
{% extends "base.html" %}

{% block title %}post_confirm_delete.html{% endblock %}

{% block content %}
<h1>Post Delete</h1>
<br>
<form action="." method="post">{% csrf_token %}
    <p>Are you sure you want to delete "{{ object }}" ?</p>
    <input type="submit" value="Confirm" class="btn btn-danger btn-sm" />
</form>
{% endblock %}
```

<br>

<br>