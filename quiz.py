import time
import random
skor=0

class Question():
  def __init__(self,soru,sık,dcevap):
    self.soru=soru
    self.sık=sık
    self.cevap=dcevap
  def showQuestion(self):
    time.sleep(1.5)
    print(self.soru)
  def showAnswers(self):
    for t in self.sık:
      time.sleep(1.5)
      print(t)

class Check(Question):
  def __init__(self,soru,sık,dcevap,vcevap):
    Question.__init__(self,soru,sık,dcevap)
    self.verilen=vcevap
  def check(self):
    if self.cevap==self.verilen:
      self.flag=1
      time.sleep(1.5)
      print("doğru bildiniz.")
    else: 
      time.sleep(1.5)
      print("yanlış bildiniz.")
      self.flag=0

def func(liste,sınıf1,sınıf2):
  global skor
  random.shuffle(liste)
  for an in liste:
    uygula=sınıf1(an[0],an[1],an[2])
    uygula.showQuestion()
    uygula.showAnswers()
    cevap=input("cevabınızı yazınız:").strip().upper()
    uygula1=sınıf2(an[0],an[1],an[2],cevap)
    uygula1.check()
    if uygula1.flag==1:
      skor +=1
 
soru1="Soru-Dünyanın en büyük deniz kazalarından biri olarak tarihe geçti. 1912 yılında 1.550 kişiye mezar olan ünlü transatlantiğin adı nedir? Ödüllü Filmlere konu olmuştur?"
sık1=["A-)Titanic","B-)Hızlı ve Öfkeli","C-)Cizgili pijamalı cocuklar"]
cevap1="A"
soru2="Soru-Türkiye'nin uluslar arası telefon kodu kaçtır?"
sık2=["A-)+71","B-)+530","C-)+90"]
cevap2="C"
soru3="Soru-Tarihin sıfır noktası olarak bilinen, insanlık tarihinin ilk somut kalıntılarının bulunduğu Göbekli tepe hangi ilimizdedir?"
sık3=["A-)Usak","B-)Bursa","C-)Sanlıurfa"]
cevap3="C"
sorular=[soru1,soru2,soru3]
sıklar=[sık1,sık2,sık3]
cevaplar=[cevap1,cevap2,cevap3]

ılk=[[soru1,sık1,cevap1],[soru2,sık2,cevap2],[soru3,sık3,cevap3]]
random.shuffle(ılk)

func(ılk,Question,Check)

ılk.clear()

soru1="Soru-Ankara ne zaman başkent oldu?"
sık1=["A-)1925","B-)1920","C-)1923"]
cevap1="C"
soru2="Soru-Çanakkale zaferi hangi şavaşa aittir?"
sık2=["A-)Kurtuluş savası","B-)I. Dünya savaşı","C-)II.Balkan savaşı"]
cevap2="B"
soru3="Soru-2003 yılında Euro Vizyon yarışmasında ülkemizi temsil eden yarışmacı kimdir?"
sık3=["A-)Grup Athena","B-)Sertap Erener","C-)Ajda Pekkan"]
cevap3="B"
ılk=[[soru1,sık1,cevap1],[soru2,sık2,cevap2],[soru3,sık3,cevap3]]
random.shuffle(ılk)

func(ılk,Question,Check)

ılk.clear()

soru1="Soru-2017 yılında ilk kez sigortalı çalışmaya başlayan 25 yaşında bir erkek,Türkiye'de kaç yıl daha çalışırsa emekli olmaya hak kazanır?"
sık1=["A-)35-40","B-)25-29","C-)30-34"]
cevap1="A"
soru2="Soru-Küçük Prens aslı hikayenin yazarı kimdir?"
sık2=["A-)Charles Dickens","B-)Samed Behrengi","C-)Antoine de Saint-Exupery"]
cevap2="C"
soru3="Soru-Verilen illerimizden hangileri aynı bölgededir?"
sık3=["A-)Manisa-Balıkesir","B-)Osmanyaniye-Malatya","C-)Çorum-Amasya"]
cevap3="C"

ılk=[[soru1,sık1,cevap1],[soru2,sık2,cevap2],[soru3,sık3,cevap3]]
random.shuffle(ılk)
func(ılk,Question,Check)

ılk.clear()

soru1="Soru-Aspirinin ana maddesi nedir?"
sık1=["A-)Söğüt","B-)Köknar","C-)Kavak"]
cevap1="A"
soru2="Soru-Facebook hangi üniversitede kurulmuştur?"
sık2=["A-)Oxford","B-)Stanford","C-)Harvard"]
cevap2="C"
soru3="Soru-Hangi ülkenin iki tane başkenti vardır?"
sık3=["A-)Güney Afrika","B-)Senegal","C-)El Salvador"]
cevap3="A"

ılk=[[soru1,sık1,cevap1],[soru2,sık2,cevap2],[soru3,sık3,cevap3]]
random.shuffle(ılk)
func(ılk,Question,Check)

ılk.clear()
print(skor)