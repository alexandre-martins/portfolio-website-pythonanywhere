from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length = 100, default='')
    location = models.CharField(max_length = 200, default='')
    profile_picture = models.ImageField(upload_to='media/profile/')

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length = 20)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length = 100)
    overview = RichTextField(blank=True, null=True, config_name='overview')
    timestamp = models.DateTimeField(auto_now_add = True)
    content = RichTextUploadingField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='media/post_list_pic/')
    categories = models.ManyToManyField(Category)
    like_count = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
