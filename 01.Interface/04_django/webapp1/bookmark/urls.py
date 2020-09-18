from django.urls import path
from bookmark.views import *

app_name = 'bookmark'  # 해당 애플리케이션의 네임스페이스명


# mysite/urls.py의 path 뒷부분이 온다.
urlpatterns = [
    path('', BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', BookmarkDV.as_view(), name='detail'),

    # Example: /bookmark/add/
    path('add/', BookmarkCreateView.as_view(), name="add"),

    # Example: /bookmark/change/
    path('change/', BookmarkChangeLV.as_view(), name="change"),

    # Example: /bookmark/99/update/
    path('<int:pk>/update/', BookmarkUpdateView.as_view(), name="update"),

    # Example: /bookmark/99/delete/
    path('<int:pk>/delete/', BookmarkDeleteView.as_view(), name="delete"),

]
