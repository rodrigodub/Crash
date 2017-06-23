from django.db import models


# Create your models here.
class CCBattery(models.Model):
    name = models.CharField(max_length=30)
    state = models.IntegerField(default=0)
    positive = models.IntegerField(default=0)
    negative = models.IntegerField(default=0)

    def switch(self):
        if self.state == 0:
            self.state = 1
            self.positive = 1
            self.negative = 1
        else:
            self.state = 0
            self.positive = 0
            self.negative = 0

    def report(self):
        return '-------------\nBattery {}\nState: {}\nPositive: {}\nNegative: {}\n-------------'\
            .format(self.name, self.state, self.positive, self.negative)


class CCTransistor(models.Model):
    """Class to define a Transistor with 3 electrodes."""
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

    def report(self):
        return '-------------\nTransistor\nCollector: {}\nBase: {}\nEmitter: {}\n-------------'\
            .format(self.collector, self.base, self.emitter)


class CCCircuit(models.Model):
    """Class to define Circuits. Circuits are made of a number of components."""
    name = models.CharField(max_length=30)


class CCConection(models.Model):
    circuit = models.ForeignKey(CCCircuit, db_index=True)
    order = models.IntegerField(default=0)
    transistor1 = models.ForeignKey(CCTransistor, db_index=True, related_name='connection_from')
    transistor1field = models.CharField(max_length=10)
    transistor2 = models.ForeignKey(CCTransistor, db_index=True, related_name='connection_to')
    transistor2field = models.CharField(max_length=10)