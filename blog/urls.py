from django.conf.urls import url
from . import views

urlpatterns = [
	# This regular expression will match ^ (a beginning) followed by $ (an end)
	# so only an empty string will match.

	# That's correct, because in Django URL resolvers,
	# 'http://127.0.0.1:8000/' is not a part of the URL.

	# This pattern will tell Django that views.post_list is the right place to go
	# if someone enters your website at the 'http://127.0.0.1:8000/' address.
	url(r'^$', views.post_list, name="post_list"),

	# it starts with ^ again – "the beginning".
	# post/ just means that after the beginning, the URL should contain the word post and a /.
	# (?P<pk>\d+) – this part is trickier. It means that Django will take everything that you place here
	# and transfer it to a view as a variable called pk.

	# (Note that this matches the name we gave the primary key variable back in blog/templates/blog/post_list.html!)
	# \d also tells us that it can only be a digit, not a letter (so everything between 0 and 9).
	url(r'article/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	]
