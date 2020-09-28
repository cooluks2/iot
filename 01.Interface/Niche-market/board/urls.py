from django.urls import path, re_path
from board.views import *
from django.contrib import admin

app_name = 'board'

urlpatterns = [
    path('<int:pk>', BoardView.as_view(), name='board'),
    path('board_detail/<int:pk>', BoardViewDV.as_view(), name='board_detail'),
    path('board_add/<int:fk>/', BoardCreateView.as_view(), name="board_add"),
    path('board_update/<int:pk>/', BoardUpdateView.as_view(), name="board_update"),
    path('board_delete/<int:pk>/', BoardDeleteView.as_view(), name="board_delete"),
]