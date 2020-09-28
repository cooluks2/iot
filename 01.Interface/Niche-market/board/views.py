from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from board.models import Board, models
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, \
    TodayArchiveView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from mysite.views import OwnerOnlyMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from market.models import Market, Store, MarketAttachFile, StoreAttachFile, StoreComment


# TemplateView
class BoardView(ListView):
    model = Board

    def get(self, request, *args, **kwargs):
        queryset = Board.objects.filter(market_id=kwargs['pk']).order_by('id')
        page = int(request.GET.get('p', 1))
        paginator = Paginator(queryset, 5)
        boards = paginator.get_page(page)

        ctx = {
            'boards': boards,
            'market_fk': kwargs['pk'],

        }
        return render(request, 'board_list.html', ctx)


class BoardViewDV(DetailView):
    def get(self, request, *args, **kwargs):
        queryset = Board.objects.get(pk=kwargs['pk'])
        ctx={
            'board': queryset,
        }
        return render(request, 'board_detail.html', ctx)


class BoardCreateView(LoginRequiredMixin, CreateView):
    model = Board
    template_name = 'board_form.html'
    fields = ['title', 'content']

    success_url = reverse_lazy('market:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.market = Market.objects.get(pk=self.kwargs.get('fk'))
        # form.instance.modify_dt = timezone.now()  # 업데이트 시간 버그 문제
        response = super().form_valid(form)  # Post 모델 저장, self.object
        return response



class BoardUpdateView(OwnerOnlyMixin, UpdateView):
    model = Board
    template_name = 'board_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('market:home')

    def form_valid(self, form):
        return super().form_valid(form)


class BoardDeleteView(OwnerOnlyMixin, DeleteView):
    model = Board
    success_url = reverse_lazy('market:home')
    template_name = 'board_confirm_delete.html'
