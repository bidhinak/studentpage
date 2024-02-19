from django.contrib import admin

from stdapp import models

# Register your models here.
admin.site.register(models.Login)
admin.site.register(models.teacher)
admin.site.register(models.student)