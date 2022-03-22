
from django.db import models

# Create your models here.
from model_utils import Choices
from model_utils.fields import StatusField


class Operator(models.Model):

        name = models.CharField(max_length=30)
        surname = models.CharField(max_length=30)
        email = models.EmailField()
        STATUS = Choices('attivo', 'non attivo', 'occupato')
        status = StatusField()

        def __str__(self):
            return self.name + " " + self.surname

        class Meta:
            verbose_name = "Operator"
            verbose_name_plural = "Operators"





class ConfigSlot(models.Model):
        slot_time_value = models.IntegerField()

        def __str__(self):
            return str(self.slot_time_value) + " minutes"


class ConfigOperator(models.Model):
    id_operator = models.ForeignKey(Operator, on_delete=models.CASCADE, related_name="operator_config")
    id_slot = models.ForeignKey(ConfigSlot, on_delete=models.CASCADE, related_name="slot_num")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

