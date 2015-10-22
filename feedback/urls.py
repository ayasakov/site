from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.feedbackView, name='feedback'),
    url(r'^send/$', views.sendView, name='send'),
    url(r'^a5d491060952aa8ad5fdee071be752de/$', views.commentsView, name='comments'),
    url(r'^06d4cd63bde972fc66a0aed41d2f5c51/(?P<commentId>[0-9]+)/$', views.commentView, name='comment'),
]
