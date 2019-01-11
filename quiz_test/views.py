
from rest_framework import generics
from .serializers import QuestionSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status

from .decorators import validate_request_data
from .models import Question, Sub_Topic
from .serializers import QuestionSerializer, Sub_TopicSerializer
from json import loads
import json

#class ListQuestionView(generics.ListAPIView):
#    queryset = Question.objects.all()
#    serializer_class = QuestionSerializer

class ListCreateQuestionView(generics.ListCreateAPIView):
    """
    GET questions/
    POST questions/
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @validate_request_data
    def post(self, request, *args, **kwargs):
        a_question = Question.objects.create(
            parentid = request.data["parentid"],
            qid=request.data["qid"],
            question=request.data["question"],
            a= request.data["a"],
            b= request.data["b"],
            c= request.data["c"],
            d= request.data["d"],
            answer = request.data["answer"],
            importance = request.data["importance"],
            complexity = request.data["complexity"],
            time = request.data["time"],
            marks = request.data["marks"],
            foundation = request.data["foundation"],
            subject = request.data["subject"],
            core =  request.data["core"],
            exam = request.data["exam"],
            fscore = request.data["fscore"],
            sscore = request.data["sscore"],
            cscore = request.data["cscore"],
            escore = request.data["escore"]
        )
        return Response(
            data=QuestionSerializer(a_question).data,
            status=status.HTTP_201_CREATED
        )

class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET questions/:id/
    PUT questions/:id/
    DELETE questions/:id/
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request, *args, **kwargs):
        try:
            a_question = self.queryset.get(pk=kwargs["pk"])
            return Response(QuestionSerializer(a_question).data)
        except Question.DoesNotExist:
            return Response(
                data={
                    "message": "Question with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_request_data
    def put(self, request, *args, **kwargs):
        try:
            a_question = self.queryset.get(pk=kwargs["pk"])
            serializer = QuestionSerializer()
            updated_question = serializer.update(a_question, request.data)
            return Response(QuestionSerializer(updated_question).data)
        except Question.DoesNotExist:
            return Response(
                data={
                    "message": "Question with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_squestion = self.queryset.get(pk=kwargs["pk"])
            a_question.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Question.DoesNotExist:
            return Response(
                data={
                    "message": "Question with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class ListCreateSub_TopicView(generics.ListCreateAPIView):
    """
    GET songs/
    POST songs/
    """
    queryset = Sub_Topic.objects.all()
    serializer_class = Sub_TopicSerializer

    @validate_request_data
    def post(self, request, *args, **kwargs):
        a_sub_topic = Sub_Topic.objects.create(
            staticid=request.data["staticid"],
            sub_topic=request.data["sub_topic"]
        )
        return Response(
            data=Sub_TopicSerializer(a_sub_topic).data,
            status=status.HTTP_201_CREATED
        )


class Sub_TopicDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET sub_topic/:id/
    PUT sub_topic/:id/
    DELETE sub_topic/:id/
    """
    #queryset = Sub_Topic.objects.all()
    serializer_class = Sub_TopicSerializer

    def get(self, request, *args, **kwargs):
        try:
            data = {}
            i = 0
            for res in Sub_Topic.objects.filter(staticid =kwargs["pk"]):
                data[i] =[]
                data[i].append({
                    'sub_topic' : res.sub_topic,'static_id':res.staticid})
                i = i+1
                result = json.dumps(data)             
            return Response(json.loads(result))
            #data = dict(loads(json_data))
            #data = Sub_Topic.objects.all().filter(staticid = 1)
            #user_count = Sub_Topic.objects.count()
            #content = {'user_count': user_count}
            #a_sub_topic = self.queryset.get(pk=kwargs["pk"])
            #serializer = Sub_TopicSerializer(data)
            #print(serializer.data)
            #return Response(1)
        except Sub_Topic.DoesNotExist:
            return Response(
                data={
                    "message": "Sub_Topic with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_request_data
    def put(self, request, *args, **kwargs):
        try:
            a_sub_topic = self.queryset.get(pk=kwargs["pk"])
            serializer = Sub_TopicSerializer()
            updated_sub_topic = serializer.update(a_sub_topic, request.data)
            return Response(Sub_TopicSerializer(updated_sub_topic).data)
        except Sub_Topic.DoesNotExist:
            return Response(
                data={
                    "message": "Sub_Topic with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_sub_topic = self.queryset.get(pk=kwargs["pk"])
            a_sub_topic.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Sub_Topic.DoesNotExist:
            return Response(
                data={
                    "message": "Sub_Topic with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )