from django.contrib import admin
from tracker import models

# Register your models here.
admin.site.register(models.Course)
admin.site.register(models.Assignment)
