
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import Thread, Post


class ThreadListView(ListView):
    model = Thread


class ThreadDetailView(DetailView):
    model = Thread


class CreateThreadView(CreateView):
    model = Thread
    fields = ['title']
    success_url = reverse_lazy('thread_list')
    #Метод get_success_url в Django возвращает url-ссылку,
    # на которую будет осуществляться переход после успешной обработки формы

    # reverse_lazy в Django используется, когда путь нужно получить на этапе инициализации программы


class CreatePostView(CreateView):
    model = Post
    fields = ['content']

    def form_valid(self, form):
        form.instance.thread_id = self.kwargs['pk']
        #ссылка на экземпляр модели
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('thread_detail', kwargs={'pk': self.kwargs['pk']})
def index(request):
    return render(request,'mainly/index.html')
def about(request):
    return render(request,'mainly/about.html')


