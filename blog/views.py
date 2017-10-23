from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

# function (def) called post_list that takes request and return a 
# function render that will render (put together) our template blog/post_list.html
def post_list(request):
	# sort and filter post with published_date
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	# {} is for template name using it for template in HTML
	return render(request, 'blog/post_list.html', {'posts': posts})