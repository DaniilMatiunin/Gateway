from django.db import models

class Thread(models.Model):
    title = models.CharField('Название', max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    content = models.TextField('Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.thread

