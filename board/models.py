from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Topic(models.Model):#Topic that useer can create and the link post # TODO:
    title = models.CharField(max_length = 500)
class Post(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING,)
    topic = models.ForeignKey(Topic,on_delete=models.DO_NOTHING,)
