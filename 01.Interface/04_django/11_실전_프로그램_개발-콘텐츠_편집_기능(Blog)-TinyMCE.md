# 실전 프로그램 개발 - 콘텐츠 편집 기능 - (Blog, TinyMCE)

<br>

### Django TinyMCE

**\<textarea\>**

-   단순 텍스트 입력 및 출력 만 지원

**워드프로세스와 같은 스타일 적용이 가능한 편집기 필요**

-   웹 에디터
    -   TinyMCE 
    -   https://www.tiny.cloud/

![image-20201007095928311](11_실전_프로그램_개발-콘텐츠_편집_기능(Blog)-TinyMCE.assets/image-20201007095928311.png)  

<br>

**django-tinymce 패키지**

-   장고의 앱으로 tinymce 지원
-   `pip install django-tinymce`

<br>

**mysite/settings.py**

```python
INSTALLED_APPS = [
    :
    'taggit_templatetags2',
    'widget_tweaks',
    'tinymce',
    :
]
```

<br>

**mysite/urls.py**

```python
:
urlpatterns = [
 :
    path('tinymce/', include('tinymce.urls')),
]
```

<br>

**blog/models.py**

```python
  :
from tinymce.models import HTMLField

class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    content = HTMLField('CONTENT') #models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
    tags = TaggableManager(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)
    read_cnt = models.IntegerField('READ COUNT', default=0)
    :
```

<br>

**blog/templates/post/post_form.html**

```html
:
</form>
{% endblock %}

{% block extra-script %}
    <script src="https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js" referrerpolicy="origin"></script>
    <script>
        tinymce.init({
            selector:'textarea',
            menubar: false,
            statusbar: false,
            toolbar1: 'formatselect | bold italic strikethrough forecolor backcolor | link | alignleft aligncenter alignright alignjustify | numlist bullist outdent indent | removeformat'
        });
    </script>
{% endblock %}
```

<br>

**blog/templates/post/post_detail.html**

```html
<div>
    {{ post.content | linebreaks}}
</div>
```

-   safe 필터
    -   HTML 태그 내용을 HTML로 처리

```html
<div>
    {{ post.content | safe }}
</div>
```

<br>