
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from bs4 import BeautifulSoup
import requests
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

def data_parsing(request):
    url="https://www.rudn.ru/contacts"
    connect= requests.get(url)
    print(connect)
    HTML=BeautifulSoup(connect.text,'html.parser')
    contacts=[]
    phonez_numer=HTML.find_all("div",class_="contacts__item mail")

    n=['data','fotos','fotodwdw']
    data ={
        'key':
        'phone': contacts
    }
    return render(request,'app/data_parsing.html',data)



