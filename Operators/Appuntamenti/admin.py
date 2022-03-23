from django.contrib import admin

from .models import Operator, ConfigSlot, ConfigOperator



admin.site.register(Operator)
admin.site.register(ConfigSlot)
admin.site.register(ConfigOperator)

# Register your models here.
