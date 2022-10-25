import requests
import json
base="https://api.themoviedb.org/3/movie/now_playing?api_key=fde9ebaa0258b656561cbfd3bba30bfc"
 
populer=requests.get(base)
populer=populer.text
populer=json.loads(populer)
print("populer fimler;")
a=1
for pop in populer["results"]:
    print(str(a)+"-"+pop["original_title"])
    a=a+1
istenen=input("hangi filmin yorumlarına bakmak istersiniz: ")
for k in populer["results"]:
    if (k["original_title"]==istenen):
        print(k["overview"])
        