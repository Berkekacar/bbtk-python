import datetime
import time

# def measure(text,girdi): 
#     if not text==girdi:
#         raise Exception("Girdiğiniz yazı metin ile uyuşmamaktadır.")
text="mustafa kemal atatürk"
print(f"Hız hesaplama '{text}' Metnini ne kadar hızlı yazabilirsin.\nHadi başlayalım.")
time.sleep(1.5)
print("Hazır mısın?")
time.sleep(1.5)
print("Haydı başlayalım o zaman.")
before=datetime.datetime.now()
girdi=input("metni giriniz:")
# try:
#     measure(text,girdi)
# except Exception as ex:
#     print(ex)
# else:
#     if text==girdi:
#         after=datetime.datetime.now()
#         sure=(after-before)
#         print(sure)  
baslangıc=datetime.datetime.now()
def func(text,baslangıc):
    girdi=input("metni giriniz:")
    
    if text==girdi:
        sonlanma=datetime.datetime.now()
        print(sonlanma-baslangıc)
    elif girdi.strip()=="q":
        print("atanın adını beceremeyip çıkıyor musun ?")
    else:
        print("yanlış bir daha dene (q programı sonlandırır)")
        func(text)


func(text,baslangıc)