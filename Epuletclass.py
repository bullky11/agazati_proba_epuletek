class Epulet:
    def __init__(self,sor):
        self.nev=sor[0]
        self.varos=sor[1]
        self.orszag=sor[2]
        self.magassag=float(sor[3])
        self.emelet=int(sor[4])
        self.epult=int(sor[5])

    def __str__(self):
      return  f"{self.nev},{self.varos},{self.orszag},{self.magassag},{self.emelet},{self.epult},"