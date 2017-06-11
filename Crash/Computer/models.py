from django.db import models


# Create your models here.
class CCTransistor(models.Model):
    """Class to define a Transistor with 3 electrodes"""
    # collector
    electrode_in = models.IntegerField(default=0)
    # emitter
    electrode_out = models.IntegerField(default=0)
    # base
    gate = models.IntegerField(default=0)

    def update(self):
        if self.gate and self.electrode_in:
            self.electrode_out = 1
        else:
            self.electrode_out = 0

