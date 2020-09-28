from django.shortcuts import render, get_object_or_404, redirect
from market.models import Market, Store, MarketAttachFile, StoreAttachFile, StoreComment
from django.views.generic import TemplateView, DetailView, View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from mysite.views import OwnerOnlyMixin
from django.http import FileResponse
import os
from django.conf import settings
from django.core.paginator import Paginator
import json
import urllib.request
from django.utils import timezone


class MarketDetail(DetailView):
    def get(self, request, *args, **kwargs):
        queryset = get_object_or_404(Market, pk=kwargs['pk'])
        ctx = {
            'market': queryset
        }
        return render(request, 'market/market_detail.html', ctx)


class MarketDV(View):

    def get(self, request, *args, **kwargs):
        queryset3 = get_object_or_404(Market, pk=kwargs['pk'])
        # 네이버 블로그 크롤링 추가
        client_id = "un73j8VyJzJJfWpGfFWD"
        client_secret = "FPdfimL0ui"

        q = queryset3.market_name  # 시장이름으로만 블로그 내에 검색
        encText = urllib.parse.quote(q)
        url = "https://openapi.naver.com/v1/search/blog?query=" + encText + "&display=4"  # json 결과, 출력결과 4개
        market_request = urllib.request.Request(url)
        market_request.add_header("X-Naver-Client-Id", client_id)
        market_request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(market_request)
        rescode = response.getcode()

        if (rescode == 200):
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            items = result.get('items')

            context = {
                'items': items,  # 크롤링 검색 결과
                'market_detail': queryset3
            }
            return render(request, 'market/market.html', context=context)


class MarketCreateView(LoginRequiredMixin, CreateView):
    model = Market
    template_name = 'market/market_form.html'
    # introduction 빠져서 임시적인 주석처리
    # fields = ['market_name', 'introduction', 'location']
    fields = '__all__'

    def get_success_url(self):
        return reverse('market:market', kwargs={'pk': self.object.pk})

    def form_valid(self, form):

        form.instance.owner = self.request.user
        response = super().form_valid(form)

        files = self.request.FILES.getlist("files")
        for file in files:
            attach_file = MarketAttachFile(market=self.object, filename=file.name, size=file.size,
                                           content_type=file.content_type, upload_file=file)
            attach_file.save()
        return response


class MarketUpdateView(OwnerOnlyMixin, UpdateView):
    model = Market
    fields = '__all__'

    def get_success_url(self):
        return reverse('market:market', kwargs={'pk': self.object.pk})


    def form_valid(self, form):
        form.instance.owner = self.request.user


        # 파일 삭제
        # delete_files = self.request.POST["delete_files"]
        delete_files = self.request.POST.getlist("delete_files")
        for fid in delete_files:  # fid는 문자열 타입임
        # 실제 파일 삭제 및 PostAttachFile 삭제
            file = MarketAttachFile.objects.get(id=int(fid))
            file_path = os.path.join(settings.MEDIA_ROOT, str(file.upload_file))
            os.remove(file_path)  # 실제 파일 삭제
            file.delete()  # 모델 삭제(테이블의 행 삭제)


        response = super().form_valid(form)  # Post 모델 저장, self.object

        # 업로드 파일 얻기
        files = self.request.FILES.getlist("files")
        for file in files:
            attach_file = MarketAttachFile(market=self.object, filename=file.name, size=file.size, content_type=file.content_type, upload_file=file)
            attach_file.save()
        return response

class MarketDeleteView(OwnerOnlyMixin, DeleteView):
    model = Market
    success_url = reverse_lazy('market:home')



class StoreLV(ListView):
    model = Store

    def get(self, request, *args, **kwargs):
        queryset = Store.objects.filter(market_list_id=kwargs['pk']).order_by('id')
        page = int(request.GET.get('p', 1))
        paginator = Paginator(queryset, 5)
        boards = paginator.get_page(page)

        ctx = {
            'boards': boards,
            'market_fk': kwargs['pk'],

        }
        return render(request, 'market/store_list.html', ctx)


class StoreDV(DetailView):
    def get(self, request, *args, **kwargs):
        queryset = StoreComment.objects.filter(store_id=kwargs['pk'])
        queryset2 = Store.objects.get(pk=kwargs['pk'])

        page = int(request.GET.get('p', 1))     # 댓글 페이징
        paginator = Paginator(queryset, 4)
        commments = paginator.get_page(page)

        ctx={
            'comments': commments,
            'store': queryset2,
        }
        return render(request, 'market/store_detail.html', ctx)


class StoreCreateView(LoginRequiredMixin, CreateView):
    model = Store
    template_name = 'market/store_form.html'
    fields = ['store_name', 'store_introduction', 'open_hour', 'close_hour', 'hour_information']
    success_url = reverse_lazy('market:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.market_list = Market.objects.get(pk=self.kwargs.get('fk'))
        # form.instance.modify_dt = timezone.now()  # 업데이트 시간 버그 문제
        response = super().form_valid(form)  # Post 모델 저장, self.object

        # 업로드 파일 얻기
        files = self.request.FILES.getlist("files")
        for file in files:
            attach_file = StoreAttachFile(post=self.object, filename=file.name,
                                          size=file.size, content_type=file.content_type,
                                          upload_file=file)
            attach_file.save()
        return response

        # return super().form_valid(form)



class StoreUpdateView(OwnerOnlyMixin, UpdateView):
    model = Store
    fields = ['store_name', 'store_introduction', 'open_hour', 'close_hour', 'hour_information']
    success_url = reverse_lazy('market:home')


    def form_valid(self, form):
        form.instance.owner = self.request.user

        # 파일 삭제
        # delete_files = self.request.POST["delete_files"]
        delete_files = self.request.POST.getlist("delete_files")
        for fid in delete_files:  # fid는 문자열 타입임
        # 실제 파일 삭제 및 PostAttachFile 삭제
            file = StoreAttachFile.objects.get(id=int(fid))
            file_path = os.path.join(settings.MEDIA_ROOT, str(file.upload_file))
            os.remove(file_path)  # 실제 파일 삭제
            file.delete()  # 모델 삭제(테이블의 행 삭제)

        response = super().form_valid(form)  # Post 모델 저장, self.object

        # 업로드 파일 얻기
        files = self.request.FILES.getlist("files")
        for file in files:
            attach_file = StoreAttachFile(post=self.object, filename=file.name, size=file.size, content_type=file.content_type, upload_file=file)
            attach_file.save()
        return response

class StoreDeleteView(OwnerOnlyMixin, DeleteView):
    model = Store
    success_url = reverse_lazy('market:home')


def market_download(request, id):
    file = MarketAttachFile.objects.get(id=id)
    file_path = os.path.join(settings.MEDIA_ROOT, str(file.upload_file))
    return FileResponse(open(file_path, 'rb'))


def store_download(request, id):
    file = StoreAttachFile.objects.get(id=id)
    file_path = os.path.join(settings.MEDIA_ROOT, str(file.upload_file))
    return FileResponse(open(file_path, 'rb'))


# 댓글 등록 함수
def store_comment(request, pk, fk):
    store = Store.objects.get(pk=pk)
    comments = StoreComment()
    comments.author = request.user
    comments.comment = request.GET['comments']
    comments.registered_date = timezone.datetime.now()
    comments.score = request.GET['score']
    comments.store = store
    comments.save()
    return redirect('market:store_detail', fk, pk)
