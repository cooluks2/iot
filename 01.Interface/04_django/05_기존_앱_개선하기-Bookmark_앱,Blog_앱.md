# 기존 앱 개선하기 - Bookmark 앱, Blog 앱 -

<br>

### 기존 앱 개선 설계하기

**Bookmark**

![image-20201006144357877](05_기존_앱_개선하기-Bookmark_앱,Blog_앱.assets/image-20201006144357877.png)  

<br>

**Blog**

![image-20201006144421502](05_기존_앱_개선하기-Bookmark_앱,Blog_앱.assets/image-20201006144421502.png)  

<br>

**작업 절차**

![image-20201006144445797](05_기존_앱_개선하기-Bookmark_앱,Blog_앱.assets/image-20201006144445797.png)  

<br>

### 개발 코딩하기

**bookmark/templates/bookmark/bookmark_list.html**

```html
{% extends "base.html" %}

{% block title %}bookmark_list.html{% endblock %}

{% block content %}

<h1>Bookmark List</h1>
<br>
<ul>
    {% for bookmark in object_list %}
    <li><a href="{% url 'bookmark:detail' bookmark.id %}">
        {{ bookmark }}</a></li>
    {% endfor %}
</ul>

{% endblock %}
```

<br>

**bookmark/templates/bookmark/bookmark_detail.html**

```html
{% extends "base.html" %}

{% block title %}bookmark_detail.html{% endblock %}

{% block content %}

<h1>{{ object.title }}</h1>
<ul>
    <li>URL: <a href="{{ object.url }}">{{ object.url }}</a></li>
</ul>
<a href="{% url 'bookmark:index' %}">목록으로</a>

{% endblock %}
```

<br>

**blog/templates/blog/post_all.html**

```html
{% extends "base.html" %}

{% block title %}post_all.html{% endblock %}

{% block content %}
<h1>Blog List</h1>
<br>
{% for post in posts %}
<h3><a href='{{ post.get_absolute_url }}' target="_blank">
    {{ post.title }}</a></h3>
{{ post.modify_date|date:"N d, Y" }}
<p>{{ post.description }}</p>
{% endfor %}
<br>
<div>
    <span>
        {% if page_obj.has_previous %}
        <a href="?page={{ page_obj.previous_page_number }}">PreviousPage</a>
        {% endif %}
        Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}
        {% if page_obj.has_next %}
        <a href="?page={{ page_obj.next_page_number }}">NextPage</a>
        {% endif %}
    </span>
</div>
{% endblock %}
```

<br>

**blog/templates/blog/post_detail.html**

```html
{% extends "base.html" %}

{% block title %}post_detail.html{% endblock %}

{% block content %}
<h2>{{ object.title }}</h2>
<p>
    {% if object.get_next %}
    <a href="{{ object.get_next.get_absolute_url }}"
       title="View previous post">
        <i class="fas fa-arrow-circle-left"></i> {{ object.get_next }}
    </a>
    {% endif %}
    {% if object.get_previous %}
    | <a href="{{ object.get_previous.get_absolute_url }}"
         title="View next post">
    {{ object.get_previous }} <i class="fas fa-arrow-circle-right"></i>
    </a>
    {% endif %}
</p>
<div>{{ object.modify_dt|date:"j F Y" }}</div>
<br>
<div>
    {{ object.content|linebreaks }}
</div>
{% endblock %}
```

<br>

**blog/templates/blog/post_archive.html**

```html
{% extends "base.html" %}

{% block title %}post_archive.html{% endblock %}

{% block content %}

<h1>Post Archives until {% now "b d, Y" %}</h1>
{% for date in date_list %}
<a href="{% url 'blog:post_year_archive' date|date:'Y' %}"
   class="btn btn-outline-primary btn-sm mx-1">
    Year-{{ date|date:"Y" }}</a>
{% endfor %}
<br><br>
<div>
    <ul>
        {% for post in object_list %}
        <li class="h5">
            {{ post.modify_dt|date:"Y-m-d" }}&emsp;
            <a href="{{ post.get_absolute_url }}">
                <strong>{{ post.title }}</strong></a>
        </li>
        {% endfor %}
    </ul>
</div>
{% endblock %}
```

<br>

**blog/templates/blog/post_archive_year.html**

```html
{% extends "base.html" %}

{% block title %}post_archive_year.html{% endblock %}

{% block content %}

<h1>Post Archives for {{ year|date:"Y" }}</h1>
{% for date in date_list %}
<a href="{% url 'blog:post_month_archive' date|date:'Y' date|date:'b' %}"
   class="btn btn-outline-primary btn-sm mx-1">
    {{ date|date:"F" }}</a>
{% endfor %}
<br><br>
<div>
    <ul>
        {% for post in object_list %}
        <li class="h5">
            {{ post.modify_dt|date:"Y-m-d" }}&emsp;
            <a href="{{ post.get_absolute_url }}">
                <strong>{{ post.title }}</strong></a>
        </li>
        {% endfor %}
    </ul>
</div>
{% endblock %}
```

<br>

**blog/templates/blog/post_archive_month.html**

```html
{% extends "base.html" %}

{% block title %}post_archive_month.html{% endblock %}

{% block content %}
<h1>Post Archives for {{ month|date:"N, Y" }}</h1>
<br><br>
<div>
    <ul>
        {% for post in object_list %}
        <li class="h5">
            {{ post.modify_dt|date:"Y-m-d" }}&emsp;
            <a href="{{ post.get_absolute_url }}">
                <strong>{{ post.title }}</strong></a>
        </li>
        {% endfor %}
    </ul>
</div>
{% endblock %}
```

<br>

**blog/templates/blog/post_archive_day.html**

```html
{% extends "base.html" %}

{% block title %}post_archive_day.html{% endblock %}

{% block content %}
<h1>Post Archives for {{ day|date:"N d, Y" }}</h1>
<br><br>
<div>
    <ul>
        {% for post in object_list %}
        <li class="h5">
            {{ post.modify_dt|date:"Y-m-d" }}&emsp;
            <a href="{{ post.get_absolute_url }}">
                <strong>{{ post.title }}</strong></a>
        </li>
        {% endfor %}
    </ul>
</div>
{% endblock %}
```

<br>