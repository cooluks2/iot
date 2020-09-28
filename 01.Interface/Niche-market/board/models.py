from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from market.models import Market


from taggit.managers import TaggableManager

class Board(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50,)
    content = models.TextField('CONTENT')
    registered_date = models.DateTimeField('CREATE DATE', auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)

    class Meta:
        verbose_name = 'board'

        verbose_name_plural = 'boards'
        db_table = 'board'  # 테이블명 재정의
        ordering = ('-modify_dt',)  # orderby 절, -이면 내림차순

    def __str__(self):
        return self.title
