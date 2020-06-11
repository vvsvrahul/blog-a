from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class BlogContent(models.Model):
#         user = models.OneToOneField(User,on_delete=models.CASCADE)
#         Title = models.CharField(max_length = 20)
#         content = models.CharField(max_length=5000)
#         def __str__():
#             return self.user.username
#


class BlogContent11(models.Model):
        id = models.BigIntegerField(primary_key = True)
        user  = models.ForeignKey(User,related_name='stories',on_delete=models.CASCADE)
        title = models.CharField(max_length = 50)
        story = models.CharField(max_length=5000)
        def __str__(self):
            return self.user.username


class PublishUser(models.Model):
    title = models.CharField(max_length = 50)
    story = models.CharField(max_length=5000)
    author = models.CharField(max_length=100)
    def __str__(self):
        return self.title
