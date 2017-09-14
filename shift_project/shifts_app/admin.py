from django.contrib import admin
from shifts_app.shift import Shift 
from shifts_app.run import Run
from shifts_app.group import Post
# Register your models here.
admin.site.register(Shift)
admin.site.register(Run)
admin.site.register(Post)