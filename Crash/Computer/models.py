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
        return '------\nBattery {} | State: {} | Positive: {} | Negative: {}\n------'\
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
        self.save()

    def switch(self, electrode):
        # switch('c') or switch('b')  to switch the collector or the base
        if electrode.upper() == 'C':
            self.collector = (self.collector - 1) ** 2
        elif electrode.upper() == 'B':
            self.base = (self.base - 1) ** 2
        self.update()

    def report(self):
        """Display the state of all three electrodes of Transistors"""
        s1 = '              Transistor     C  B  E\n                  {}          {}  {}  {}'\
            .format(self.id, self.collector, self.base, self.emitter)
        return s1
        # return '-------------\nTransistor\nCollector: {}\nBase: {}\nEmitter: {}\n-------------'\
        #     .format(self.collector, self.base, self.emitter)


class CCCircuit(models.Model):
    """Class to define Circuits. Circuits are made of a number of components."""
    name = models.CharField(max_length=30)
    instate = models.IntegerField(default=0)
    outstate = models.IntegerField(default=0)

    def getState(self):
        """Display the state of all three electrodes of Transistors"""
        connections = CCConnection.objects.filter(circuit=self).order_by('order')
        s = ['{}\n                  Battery   Transistor   |   Transistor   Battery\n'
             '                    (+)      C  B  E     |    C  B  E       (-)\n'
             '                  -------   ---------    |   ---------    -------'.format(connections[0].circuit.name)]
        for con in connections:
            if (con.transistor2 == None) and (con.batteryfield == 'positive'):
                s.append('                     {}                   |    {}  {}  {}'.format(con.battery.positive,
                                                                                            con.transistor1.collector,
                                                                                            con.transistor1.base,
                                                                                            con.transistor1.emitter))
            elif (con.transistor2 == None) and (con.batteryfield == 'negative'):
                s.append('                             {}  {}  {}     |                   {}'.format(
                    con.transistor1.collector, con.transistor1.base, con.transistor1.emitter, con.battery.negative))
            else:
                s.append('                             {}  {}  {}     |    {}  {}  {}'.format(con.transistor1.collector,
                                                                                              con.transistor1.base,
                                                                                              con.transistor1.emitter,
                                                                                              con.transistor2.collector,
                                                                                              con.transistor2.base,
                                                                                              con.transistor2.emitter))
        return [line for line in s]

    def getConnections(self):
        """Display the connected Transistor electrodes"""
        connections = CCConnection.objects.filter(circuit=self).order_by('order')
        s = ['{}\n                  Battery   Transistor   |   Transistor   Battery\n'
             '                    (+)      C  B  E     |    C  B  E       (-)\n'
             '                  -------   ---------    |   ---------    -------'.format(connections[0].circuit.name)]
        for con in connections:
            if (con.transistor2 == None) and (con.batteryfield == 'positive'):
                if con.transistor1field == 'collector':
                    s.append('                     {}                   |    {}'.format(con.battery.positive,
                                                                                                con.transistor1.collector))
                elif con.transistor1field == 'base':
                    s.append('                     {}                   |       {}'.format(con.battery.positive,
                                                                                        con.transistor1.base))
                else:
                    s.append('                     {}                   |          {}'.format(con.battery.positive,
                                                                                           con.transistor1.emitter))
            elif (con.transistor2 == None) and (con.batteryfield == 'negative'):
                if con.transistor1field == 'collector':
                    s.append('                             {}           |                   {}'.format(con.transistor1.collector,
                                                                                                       con.battery.negative))
                elif con.transistor1field == 'base':
                    s.append('                                {}        |                   {}'.format(con.transistor1.base,
                                                                                                       con.battery.negative))
                else:
                    s.append('                                   {}     |                   {}'.format(con.transistor1.emitter,
                                                                                                       con.battery.negative))
            else:
                s.append('                             {}  {}  {}     |    {}  {}  {}'.format(con.transistor1.collector,
                                                                                              con.transistor1.base,
                                                                                              con.transistor1.emitter,
                                                                                              con.transistor2.collector,
                                                                                              con.transistor2.base,
                                                                                              con.transistor2.emitter))
        return [line for line in s]

    def update(self):
        """Update Circuit state"""
        connections = CCConnection.objects.filter(circuit=self).order_by('order')
        for con in connections:
            if con.transistor2 == None:
                pass


class CCConnection(models.Model):
    """Establishes all the connections between Transistor electrodes"""
    circuit = models.ForeignKey(CCCircuit, db_index=True)
    order = models.IntegerField(default=0)
    transistor1 = models.ForeignKey(CCTransistor, related_name='connection_from')
    transistor1field = models.CharField(max_length=10)
    transistor2 = models.ForeignKey(CCTransistor, related_name='connection_to', null=True, blank=True)
    transistor2field = models.CharField(max_length=10, null=True, blank=True)
    battery = models.ForeignKey(CCBattery, null=True, blank=True)
    batteryfield = models.CharField(max_length=8, null=True, blank=True)

