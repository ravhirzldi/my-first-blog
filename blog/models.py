from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	# " CharField " is how you define text with a limited number of characters.
	# " TextField " is for long text without a limit. (Ideal for blog contents)
	# " DateTimeField " is a date and time.
	# " ForeignKey " is a link to another model.

	def publish(self):
		self.published_date = timezone.now()
		self.save()

		# " def " means that this is a function/method and
		# " publish " is the name of the method.

	def __str__(self):
		return self.title

		# In this scenario, when we call " __str__() "
		# we will get a text (string) with a Post title.
