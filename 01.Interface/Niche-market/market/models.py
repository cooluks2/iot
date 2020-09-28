from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Location(models.Model):
    location = models.CharField(max_length=50, verbose_name="지역")

    def __str__(self):
        return self.location

    class Meta:
        db_table = "location"
        verbose_name = "지역"
        verbose_name_plural = "지역"


class Market(models.Model):

    market_name = models.CharField(verbose_name="시장이름", max_length=100)
    address = models.CharField(null=True, max_length=100)
    products = models.CharField(null=True, max_length=200)
    tel = models.CharField(null=True, max_length=100)
    sights_info = models.CharField(null=True, max_length=200)
    closed_date = models.CharField(null=True, max_length=200)
    hour_info = models.CharField(null=True, max_length=100)
    park_info = models.CharField(null=True, max_length=200)
    products = models.CharField(null=True, max_length=200)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)

    def __str__(self):
        return self.market_name

    class Meta:
        db_table = "market_list"
        verbose_name = "시장목록"
        verbose_name_plural = "시장목록"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.market_name, allow_unicode=True)
        super().save(*args, **kwargs)

class Store(models.Model):
    store_name = models.CharField('STORE NAME', max_length=100)
    store_introduction = models.CharField('STORE INTRODUCTION', null=True, max_length=100)
    open_hour = models.TimeField('OPEN HOUR', blank=True, default='00:00:00')
    close_hour = models.TimeField('CLOSE HOUR', blank=True, default='23:59:59')
    hour_information = models.CharField('HOUR INFORMATION', blank=True, null=True, max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)
    market_list = models.ForeignKey(Market, on_delete=models.CASCADE)

    class Meta:
        db_table = "store_list"
        verbose_name = "점포목록"
        verbose_name_plural = "점포목록"

    def __str__(self):
        return self.store_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.store_name, allow_unicode=True)
        super().save(*args, **kwargs)


class MarketAttachFile(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name="files", verbose_name='market', blank=True, null=True)
    upload_file = models.FileField(upload_to="%Y/%m/%d", null=True, blank=True, verbose_name="파일")
    filename = models.CharField(max_length=64, null=True, verbose_name='첨부파일명')
    content_type = models.CharField(max_length=128, null=True, verbose_name='MIME TYPE')
    size = models.IntegerField('파일크기')

    class Meta:
        db_table = "market_attach_file"

    def __str__(self):
        return self.filename


class StoreAttachFile(models.Model):
    post = models.ForeignKey(Store, on_delete=models.CASCADE,
                             related_name="files",
                             verbose_name='Store', blank=True, null=True)
    upload_file = models.FileField(upload_to="%Y/%m/%d",
                                   null=True, blank=True, verbose_name='파일')
    filename = models.CharField(max_length=64, null=True,
                                verbose_name='첨부파일명')
    content_type = models.CharField(max_length=128, null=True,
                                    verbose_name='MIME TYPE')
    size = models.IntegerField('파일 크기')

    class Meta:
        db_table = "store_attach_file"

    def __str__(self):
        return self.filename


class StoreComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    comment = models.TextField(verbose_name="댓글내용")
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name="등록 시간")
    score = models.IntegerField(null=True)

    def __str__(self):
        return self.comment

    class Meta:
        db_table = "store_comment"