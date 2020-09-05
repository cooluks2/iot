from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView
from blog.models import Post
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView

from django.views.generic import FormView
from django.db.models import Q
from django.shortcuts import render

from blog.forms import PostSearchForm

from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin

from django.utils import timezone  # 업데이트 시간 버그 문제

from blog.models import PostAttachFile, Post
from django.http import FileResponse
import os
from django.conf import settings

# ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'  # 템플릿 파일명 변경
    context_object_name = 'posts'         # 컨텍스트 객체 이름 변경(object_list)
    paginate_by = 2                       # 페이지네이션, 페이지당 문서 건 수

# DetailView
class PostDV(DetailView):
    model = Post
    context_object_name = 'post'
    #
    # def get_context_data(self, **kwargs):  # 조회수
    #     context = super().get_context_data(**kwargs)
    #     post = self.get_object()
    #     post.read_cnt += 1
    #     post.save()
    #     return context


# ArchiveView
class PostAV(ArchiveIndexView):
    model= Post
    date_field = 'modify_dt'

class PostYAV(YearArchiveView):
    model= Post
    date_field = 'modify_dt'
    make_object_list = True

class PostMAV(MonthArchiveView):
    model= Post
    date_field = 'modify_dt'
    month_format = '%m'

class PostDAV(DayArchiveView):
    model= Post
    date_field = 'modify_dt'
    month_format = '%m'

class PostTAV(TodayArchiveView):
    model= Post
    date_field = 'modify_dt'
    month_format = '%m'

#--- Tag View
class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'

class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context


#--- FormView
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = Post.objects.filter(
            Q(title__icontains=searchWord) |
            Q(description__icontains=searchWord) |
            Q(content__icontains=searchWord)
        ).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list
        return render(self.request, self.template_name, context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # fields = ['title', 'slug', 'description', 'content', 'tags']
    # initial = {'slug': 'auto-filling-do-not-input'}
    fields = ['title', 'description', 'content', 'tags']


    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.modify_dt = timezone.now()  # 업데이트 시간 버그 문제

        response = super().form_valid(form)  # Post 모델 저장, self.object

        # 업로드 파일 얻기
        files = self.request.FILES.getlist("files")
        for file in files:
            attach_file = PostAttachFile(post=self.object, filename=file.name,
                                         size=file.size, content_type=file.content_type,
                                         upload_file=file)
            attach_file.save()
        return response


class PostUpdateView(OwnerOnlyMixin, UpdateView):
    model = Post
    # fields = ['title', 'slug', 'description', 'content', 'tags']
    fields = ['title', 'description', 'content']
    success_url = reverse_lazy('blog:index')

    # def form_valid(self, form):  # 업데이트 시간 버그 문제
    #     form.instance.modify_dt = timezone.now()
    #     return super().form_valid(form)
    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.modify_dt = timezone.now()  # 업데이트 시간 버그 문제

        # 파일 삭제
        # delete_files = self.request.POST["delete_files"] 하면 하나만 삭제됨
        delete_files = self.request.POST.getlist("delete_files")
        for fid in delete_files:  # fid는 문자열 타입임
        # 실제 파일 삭제 및 PostAttachFile 삭제
            file = PostAttachFile.objects.get(id=int(fid))
            file_path = os.path.join(settings.MEDIA_ROOT, str(file.upload_file))
            os.remove(file_path)  # 실제 파일 삭제
            file.delete()  # 모델 삭제(테이블의 행 삭제)


        response = super().form_valid(form)  # Post 모델 저장, self.object

        # 업로드 파일 얻기
        files = self.request.FILES.getlist("files")
        for file in files:
            attach_file = PostAttachFile(post=self.object, filename=file.name,
                                         size=file.size, content_type=file.content_type,
                                         upload_file=file)
            attach_file.save()
        return response


class PostDeleteView(OwnerOnlyMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')


def download(request, id):
    file = PostAttachFile.objects.get(id=id)
    file_path = os.path.join(settings.MEDIA_ROOT, str(file.upload_file))

    return FileResponse(open(file_path, 'rb'))