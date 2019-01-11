from django.urls import path
from .views import ListCreateQuestionView, QuestionDetailView, ListCreateSub_TopicView, Sub_TopicDetailView


urlpatterns = [
    path('questions/', ListCreateQuestionView.as_view(), name="questions-list-create"),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name="questions-detail"),
    path('subtopics/', ListCreateSub_TopicView.as_view(), name="sub_topics-list-create"),
    path('subtopics/<int:pk>/', Sub_TopicDetailView.as_view(), name="sub_topics-detail"),
]