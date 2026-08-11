from django.contrib import admin
from .models import habbit, HabbitLog

# Register your models here.
admin.site.register(habbit)
admin.site.register(HabbitLog)