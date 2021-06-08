from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView, CreateView
from paints.models import Paint, Comment
from django.urls import reverse
from django.http import HttpResponseRedirect
from paints.forms import CommentForm

def LikeView(request, pk):
    paint = get_object_or_404(Paint, id=request.POST.get('paint_id'))
    liked = False
    if paint.likes.filter(id=request.user.id).exists():
        paint.likes.remove(request.user)
        liked= False
    else:

        paint.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('detail', args=[str(pk)]))

class PaintDetailView(DetailView):
    model = Paint
    template_name = 'paint_detail.html'


class PaintListView(ListView):
    model = Paint
    template_name = 'paint_list.html'

class CommentPageView(CreateView):
    model = Comment
    template_name = 'comment.html'
    fields = ['paint','name','comment']

class AboutPageView(TemplateView):
    model = Paint
    template_name = 'about.html'

class VideoPageView(TemplateView):
    template_name = 'video.html'