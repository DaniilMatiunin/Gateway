from django.contrib import admin
from .models import Thread
from .models import Post
admin.site.register(Thread.title)
# Register your models here.
