from django.contrib import admin
from custom_reg import models

admin.site.register(models.WorkerProfile)
admin.site.register(models.ClientProfile)
admin.site.register(models.Skill)