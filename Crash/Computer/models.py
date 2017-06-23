from django.db import models


# Create your models here.
class CCTransistor(models.Model):
    """Class to define a Transistor with 3 electrodes"""
    # collector = electrode_in
    collector = models.IntegerField(default=0)
    # emitter = electrode_out
    emitter = models.IntegerField(default=0)
    # base = gate
    base = models.IntegerField(default=0)

    def update(self):
        if self.base and self.collector:
            self.emitter = 1
        else:
            self.emitter = 0

