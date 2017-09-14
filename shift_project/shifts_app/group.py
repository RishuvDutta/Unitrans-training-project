from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from shifts_app.run import Run
from django.utils.timezone import utc, make_aware, get_default_timezone
import datetime

class Post(models.Model):
	#run = models.ForeignKey(Run, related_name='related')
    # user_id = models.IntegerField()
    runs = models.ManyToManyField(Run)
    current_user = models.IntegerField()

    @classmethod
    def make_post(cls, current_user, new_post):
    	post, created=cls.objects.get_or_create(
    		current_user=current_user
    	)
    	post.runs.add(new_post)

    @classmethod
    def delete_post(cls, current_user, new_post):
    	post, created=cls.objects.get_or_create(
    		current_user=current_user
    	)
    	post.runs.remove(new_post)

	def get_absolute_url(self):
		return reverse("shift:posts")

class History(models.Model):
    past = models.ManyToManyField(Run)
    current_user = models.IntegerField()

    @classmethod
    def add_history(cls, current_user, new_post):
        post, created=cls.objects.get_or_create(
            current_user = current_user
        )
        post.past.add(new_post)