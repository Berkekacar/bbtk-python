# 1 tas 2 kagıt 3 makas
liste=[1,2,3]
import random
class Oyun:
    

    def __init__(self,secım):
        self.secım=secım
        self.score_pc=0
        self.score_user=0
        
    def tas (self,secım,):
        if self.secım==1 and pcsecım==1:
            print(f"Skore yok {pcsecım}")
        if self.secım==1 and pcsecım==2:
            print(f"Skore bilgisayarın.{pcsecım}")
            self.score_pc +=10 
        if self.secım==1 and pcsecım==3:
            print(f"Skore senindir.{pcsecım}")
            self.score_user +=10
    def kagıt(self,secım):
        if self.secım==2 and pcsecım==1:
            print(f"Skore senindir.{pcsecım}")
            self.score_user +=10
        if self.secım==2 and pcsecım==2:
            print(f"Skore yok,berabere.{pcsecım}")
        if self.secım==2 and pcsecım==3:
            print(f"Skore bilgisayarın.{pcsecım}")
            self.score_pc +=10
    def makas(self,secım):
        if self.secım==3 and pcsecım==1:
            print(f"Skore bilgisayarın.{pcsecım}")
            self.score_pc +=10
        if self.secım==3 and pcsecım==2:
            print(f"Skore sizin.{pcsecım}")
            self.score_user +=10
        if self.secım==3 and pcsecım==3:
            print(f"Skore yok.{pcsecım}")
secım=int(input("Seçiminizi giriniz:"))
berke=Oyun(secım)
while secım in liste:
    pcsecım=random.choice(liste)
    berke.tas(secım)
    berke.makas(secım)
    berke.kagıt(secım)
    secım=int(input("Seçiminizi giriniz:"))