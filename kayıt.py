import json
import os
class UserAdmin:
    def __init__(self,username,password,mail):
        self.username=username
        self.password=password
        self.mail=mail
        self.list={}
    def register(self):
        self.list.update(username=self.username,password=self.password,mail=self.mail)
        m=self.list
        json.dumps(m)
        with open("file.json","w",encoding="utf-8") as file:
            json.dump(m,file)
    def login(self):
        pass
    def logout(self):
        pass
    def display(self):
        pass
while True:
    print("MENÜ".center(101,"*"))
    secim=input("1- kayıt\n2- giriş\n3-çıkış\n4- göster\n5-exit\nseçim:")
    if(secim=="5"):
        break
    else:
        if(secim=="1"):
            username=input("username giriniz:")
            password=input("password giriniz:")
            mail=input("mail giriniz:")
            kayıt=UserAdmin(username,password,mail) 
            kayıt.register()
            print("kayıt tamamlanmıştır")  
        elif(secim=="2"):
            kullanıcıadı=input("username:")
            şifre=input("password:")
            with open("file.json",encoding="utf-8") as file:
                data=json.load(file)
                
        elif(secim=="3"):
            pass #logout
        elif(secim=="4"):
            pass #display
        else:
            print("hatalı seçim")