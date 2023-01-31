class Avtobus():
    list_passjir = []

    def __init__(self, speed, maxkol, maxSpeeds, passajirs, svobodapopugaem,seats,vibros ,zaxod,   i=0, list_passjir=[]):
        self.speed = speed
        self.maxkol = maxkol
        self.maxSpeeds = maxSpeeds
        self.passajirs = passajirs
        self.svobodapopugaem = svobodapopugaem
        self.seats = seats
        self.vibros = vibros
        self.zaxod = zaxod
        print(self.list_passjir)
        print(speed)
        print(maxkol)
        print(maxSpeeds)
        print(passajirs)
        print(svobodapopugaem)
        print(seats)

    def posadka(self,):


            self.svobodapopugaem = self.svobodapopugaem + self.vibros
            self.svobodapopugaem = self.svobodapopugaem - self.zaxod
            print(f"Было высаженно {self.vibros} человек, теперь свободно {self.svobodapopugaem} мест")

            print(f"Было посажено {self.zaxod} человек, теперь свободно {self.svobodapopugaem} мест")
            return self.svobodapopugaem

    def zadan_famil(self, opr=0,  vopros3=0, vopros0="", i=0):
        print(opr, vopros3, vopros0)
        if vopros3 == "+":
            while i < opr:
                self.list_passjir.remove(vopros0)
                i = i + 1
                print(opr, vopros3, vopros0)
        elif vopros3 == "-":
            while i < opr:
                self.list_passjir.append(vopros0)
                i = i + 1
