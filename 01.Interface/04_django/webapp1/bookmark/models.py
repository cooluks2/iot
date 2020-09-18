from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Bookmark(models.Model):

    title = models.CharField('TITLE', max_length=100, blank=True)
    url = models.URLField('URL', unique=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


"""
이 작업과 같다.
create table Bookmark(
    title varchar(100) NULL,
    url varchar(100) UNIQUE
    );
    
id integer AUTO_INCREANMENT
    PRIMARY KEY 자동으로 들어간다.
    
그래서 컬럼 3개
"""