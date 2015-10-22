from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone

from .models import Comment


def feedbackView(request):
    return render(request, 'feedback.html')


def sendView(request):
    author = request.POST['author']
    subject = request.POST['subject']
    text = request.POST['text']
    id = Comment.objects.count() + 1

    comment = Comment(id, author, subject, text, timezone.now())
    comment.save()

    return HttpResponseRedirect(reverse('index'))


def commentsView(request):
    return render(request, 'comments.html', {'comments': Comment.objects.all()})


def commentView(request, commentId):
    comment = get_object_or_404(Comment, pk=commentId)
    return render(request, 'comment.html', {'comment': comment})
