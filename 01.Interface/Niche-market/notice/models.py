from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Notice(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)
    content = models.TextField(verbose_name="댓글내용")
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name="등록 시간")
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.content

    class Meta:
        db_table = "notice"
