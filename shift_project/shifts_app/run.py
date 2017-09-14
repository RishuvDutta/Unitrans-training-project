from django.db import models

from shifts_app.shift import Shift


class Run(models.Model):

    db_table="run"

    shift = models.ForeignKey(Shift, related_name="runs_related") 
    user_id = models.IntegerField(blank=True)

    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    def get_absolute_url(self):
        return reverse("order:list", kwargs={"id": self.id})

    def __unicode__(self):
        return u"%s (%d)" % (self.start_datetime, self.user_id)


    class Meta:
        app_label = "shifts_app"