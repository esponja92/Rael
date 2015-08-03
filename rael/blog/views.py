from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def inicio(request):
	if request.user.is_authenticated():
		return render(request, 'blog/post_list.html', {})
	else:
		return redirect('django.contrib.auth.views.login')