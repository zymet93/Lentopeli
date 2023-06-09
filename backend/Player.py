from functions import check_goal

class Player:
    _WORK_AMOUNT = 1

    def __init__(self, id, location, time, money, a_ports, profession, name, timeMax):
        self.id = id
        self.location = location
        self.time = time
        self.timeMax = timeMax
        self.money = money
        self.profession = profession
        self.a_ports = a_ports
        self.resetWork()
        self.canShuffleWork = 1
        self.name = name
        self.goal = 0

    def resetWork(self):
        self.canShuffleWork = 1
        self.canWorkAmt = self._WORK_AMOUNT

    def setGoal(self, connection):
        self.goal = check_goal(connection, self.id, self.location)
        return self.goal
