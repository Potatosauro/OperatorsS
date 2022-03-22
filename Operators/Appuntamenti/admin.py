from django.contrib import admin

from .models import Operator, ConfigSlot, ConfigOperatore



admin.site.register(Operator)
admin.site.register(ConfigSlot)
admin.site.register(ConfigOperatore)

# Register your models here.
