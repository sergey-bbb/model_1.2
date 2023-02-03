# NEWS

from django.db import models

class Author(models.Model):
    Author1 = models.CharField(max_length=255)
    Author2 = models.CharField(max_length=255)


class User(models.Model):
    User1 = models.CharField(max_length=255)
    User2 = models.CharField(max_length=255)


class Category(models.Model):
    name = models.CharField(unique = True, max_length=255)


class Post(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(null=True)
    Article = models.TextField(default = "Ожидается")
    News = models.TextField(default = "Ожидается")


class PostCategory(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(null=True)

    comment = models.TextField(default = "Нет комментов")
    comments = models.ForeignKey(Post, on_delete=models.CASCADE)
