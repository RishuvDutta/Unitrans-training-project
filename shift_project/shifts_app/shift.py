from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from django.utils.timezone import utc, make_aware, get_default_timezone
import datetime

#from shifts_app.shift_group import ShiftGroup

class ShiftManager(models.Manager):

    def create_shift(self, start_datetime, end_datetime, run_times_list):
        #run_times_list -> [{start_time=time, end_time=time},{...},{...}]
        shift = self.model(
            start_datetime = start_datetime,
            end_datetime = end_datetime,
            )
        for key in run_times_list:
                shift.run_set.all()
        return shift

    def get_absolute_url(self):
        return reverse('shift-update', kwargs={'pk': self.pk})

    def __unicode__(self):
        return "%s %s" % (self.start_datetime, self.end_datetime)

    def get_shifts_in_datetime_range(self, start_datetime, end_datetime):
        return self.objects.filter(date__range=[start_datetime, end_datetime])

class Shift(models.Model):

    #runs_related

    db_table="shift"
    objects = ShiftManager()

    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    def get_absolute_url(self):
        return reverse("shift:list")

    def __unicode__(self):
        return u"%d" % self.id

    class Meta:
        app_label = "shifts_app"
