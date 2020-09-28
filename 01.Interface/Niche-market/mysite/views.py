from django.views.generic import TemplateView
from market.models import Location, Market
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin
from .forms import SingupForm

from django.views.defaults import permission_denied
from django.shortcuts import render, get_object_or_404

import requests
from bs4 import BeautifulSoup


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        res = requests.get('https://news.seoul.go.kr/economy/archives/category/nationaleconomy-news_c1/tradition_make_c1/traditioninfo_biz_nationaleconomy-n1')
        soup = BeautifulSoup(res.content, 'html.parser')

        # queryset = get_object_or_404(Market, pk=kwargs['pk']) # 마켓에서 사진 가져옴


        title_list = []
        link_list = []
        made_time_list = []
        html_content_list = []

        for links in soup.select('div.post-lst div.child_policyDL_R'):
            title = links.select('h3.tit a')
            link = links.select('h3.tit a')
            made_time = links.select('span.time')

            title = title[0].get('title')
            link = link[0].get('href')
            made_time = made_time[0].get_text()[0:11]

            html_content = [title, link, made_time]

            # title_list.append(title)
            # link_list.append(link)
            # made_time_list.append(made_time)
            html_content_list.append(html_content)

        # post = {'title': title_list,
        #         'link': link_list,
        #         'made_time': made_time_list,
        #         'html_content': html_content_list
        #         }
        post = {
                'html_content': html_content_list
                # 'market': queryset
                }


        return render(request, 'home.html', post)


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = SingupForm
    success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/delete the object"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()  # 모델 인스턴스 얻기
        if self.request.user != self.object.owner:
            self.handle_no_permission()
        return super().get(request, *args, **kwargs)



