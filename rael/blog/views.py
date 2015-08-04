from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PostForm, UserForm
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

def register(request): #copiado do curso How To Tango With Django

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        #else:
        #    print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render(request,
            'registration/register.html',
            {'user_form': user_form, 'registered': registered} )