class Player:
    _WORK_AMOUNT = 1

    def __init__(self, id, location, time, money, a_ports, profession, name):
        self.id = id
        self.location = location
        self.time = time
        self.money = money
        self.profession = profession
        self.a_ports = a_ports
        self.resetWork()
        self.canShuffleWork = 1
        self.name = name

    def resetWork(self):
        self.canShuffleWork = 1
        self.canWorkAmt = self._WORK_AMOUNT
