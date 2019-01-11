from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User 
from django.urls import reverse
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from django.contrib.auth.models import User


class Question(models.Model):
    STATUS_CHOICES = ( 
        ('draft', 'Draft'), 
        ('published', 'Published'), 
    )
    IMPORTANCE_SCORE = (
    ('LOW','Low'),
    ('NORMAL', 'Normal'),
    ('HIGH','High'),
    )
    parentid = models.CharField(max_length=250)
    staticid = models.AutoField(primary_key=True)
    qid = models.CharField(max_length=250)
    question = models.TextField()
    a= models.CharField(max_length=250)
    b= models.CharField(max_length=250)
    c= models.CharField(max_length=250)
    d= models.CharField(max_length=250)
    answer = models.CharField(max_length=250)
    importance = models.CharField(max_length=6, choices= IMPORTANCE_SCORE, default='LOW')
    complexity = models.PositiveIntegerField(default=0)
    time = models.CharField(max_length=200)
    marks = models.CharField(max_length=200)
    foundation = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    core = models.CharField(max_length=250)
    exam = models.CharField(max_length=250)
    fscore = models.CharField(max_length=250)
    sscore = models.CharField(max_length=250)
    cscore = models.CharField(max_length=250)
    escore = models.CharField(max_length=250)

    def __str__(self):
        return "{} - {}".format(self.qid, self.question)


class Sub_Topic(models.Model):
    IMPORTANCE_SCORE = (
    ('LOW','Low'),
    ('NORMAL', 'Normal'),
    ('HIGH','High'),
    )
    staticid = models.IntegerField()
    #qid = models.IntegerField()
    sub_topic = models.CharField(max_length=250)
    Num_Of_Sub_subTopics =  models.PositiveIntegerField(default=0)
    Num_Of_Questions = models.PositiveIntegerField(default=0)
    importance = models.CharField(max_length=6, choices= IMPORTANCE_SCORE, default='LOW')
    complexity = models.PositiveIntegerField(default=0)
    prerequisite = models.CharField(max_length=250)

    def __str__(self):
        return self.sub_topic
