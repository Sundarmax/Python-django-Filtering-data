from .models import Question, Sub_Topic
from rest_framework import serializers
from .models import User
        
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('parentid','staticid','qid','question','a','b','c','d','answer',
                       'importance','complexity','time','marks',
                       'foundation','subject','core','exam','fscore','sscore','cscore','escore')

class Sub_TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_Topic
        fields = ('staticid','sub_topic')
        '''('staticid','sub_topic','Num_Of_Sub_subTopics','Num_Of_Questions',
        'importance','complexity','prerequisite')'''