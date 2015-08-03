from django.db import models
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	text = models.CharField(max_length=200)
	published_date = models.DateTimeField(default=timezone.now)

	def publish(self):
		self.save()

	def __str__(self):
		return self.text
