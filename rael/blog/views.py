from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PostForm
from .models import Post
from django.utils import timezone

# Create your views here.
def inicio(request):
	if request.user.is_authenticated():
		posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
		return render(request, 'blog/post_list.html', {'posts':posts})
	else:
		return redirect('django.contrib.auth.views.login')

def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.author = request.user
			post.save()
			return redirect('blog.views.inicio')
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form':form})