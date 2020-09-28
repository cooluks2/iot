from django.shortcuts import render
from notice.models import Notice
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from mysite.views import OwnerOnlyMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy


# TemplateView
class NoticeListView(ListView):
    model = Notice

    def get(self, request, *args, **kwargs):
        queryset = Notice.objects.all().order_by('-id')
        page = int(request.GET.get('p', 1))
        paginator = Paginator(queryset, 5)
        boards = paginator.get_page(page)

        ctx = {
            'boards': boards,

        }
        return render(request, 'notice/notice_list.html', ctx)


class NoticeDetailView(DetailView):
    def get(self, request, *args, **kwargs):
        queryset = Notice.objects.get(pk=kwargs['pk'])
        ctx = {
            'board': queryset,
        }
        return render(request, 'notice/notice_detail.html', ctx)


class NoticeCreateView(LoginRequiredMixin, CreateView):
    model = Notice
    template_name = 'notice/notice_form.html'
    fields = ['title', 'content']

    success_url = reverse_lazy('notice:notice_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)  # Post 모델 저장, self.object
        return response


class NoticeUpdateView(OwnerOnlyMixin, UpdateView):
    model = Notice
    template_name = 'notice/notice_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('notice:notice_list')

    def form_valid(self, form):
        return super().form_valid(form)


class NoticeDeleteView(OwnerOnlyMixin, DeleteView):
    model = Notice
    success_url = reverse_lazy('notice:notice_list')
    template_name = 'notice/notice_confirm_delete.html'
