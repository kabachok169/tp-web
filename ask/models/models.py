from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)

class Question(models.Model):

    title = models.CharField(max_length=200)
    text = models.TextField()
    likes = models.IntegerField(blank=True, null=True)
    dislikes = models.IntegerField()
    user = models.ForeignKey(Profile, blank=True, null=True)



    def calc_likes(self):
        return self.likes - self.dislikes


class Answer(models.Model):

    text = models.TextField()
    correct = models.BooleanField()
    question = models.ForeignKey(Question)
    user = models.ForeignKey(Profile, blank=True, null=True)




