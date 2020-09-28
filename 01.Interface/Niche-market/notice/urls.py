from django.urls import path
from notice.views import NoticeListView, NoticeDetailView, NoticeCreateView, NoticeUpdateView, NoticeDeleteView

app_name = 'notice'
urlpatterns = [
    path('', NoticeListView.as_view(), name='notice_list'),
    path('<int:pk>', NoticeDetailView.as_view(), name='notice_detail'),
    path('add/', NoticeCreateView.as_view(), name='notice_add'),
    path('<int:pk>/update/', NoticeUpdateView.as_view(), name='notice_update'),
    path('<int:pk>/delete/', NoticeDeleteView.as_view(), name='notice_delete'),
]
