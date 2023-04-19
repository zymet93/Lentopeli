class Player:
    _WORK_AMOUNT = 3

    def __init__(self, id, location, time, money, a_ports, profession, name):
        self.id = id
        self.location = location
        self.time = time
        self.money = money
        self.profession = profession
        self.a_ports = a_ports
        self.resetWork()
        self.canShuffleWork = 1
        self.worked_in_country = False
        self.name = name

    def resetWork(self):
        self.canShuffleWork = 1
        self.canWorkAmt = self._WORK_AMOUNT

    def getLocation(self):
        sql = "select ident, airport.name as 'airport_name', country.name as 'country_name', country.iso_country from airport, country where airport.iso_country=country.iso_country and ident='" + self.location + "'";
        return execute_sql(sql)[0]
