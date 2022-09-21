
import requests
import threading 
import time
from pytube import YouTube
import psycopg2 
import json
conection = psycopg2.connect(database="postgres", user="postgres", password="registro12", host="127.0.0.1", port="5432")

def registro_db(api): 
    response = requests.get(api) 
    if response.status_code == 200:
        payload = response.json()
        results = payload.get('results', [])
        if results:
            for pokemon in results:
                name = pokemon['name']
                cursor = conection.cursor()
                sql="INSERT INTO pokemones(nombre) VALUES (%s)"
                map= name
                cursor = conection.cursor()
                cursor.execute(sql,(json.dumps(map),))
                conection.commit()
            print("Base de datos actualizada")


             

def descarga(url_video):
   for x in url_video:
    yt = YouTube(x)
    video=  yt.streams.filter(file_extension='mp4').order_by('resolution').first()
    video.download(destino)
    print("descargado en: "+destino)

def get_services(x):
##print(f'Data es = {x}')
   time.sleep(0.5)
   response = requests.get('https://randomuser.me/api/')
   if response.status_code == 200:
       results = response.json().get('results',[])
       nombre = results[0].get('name').get('first')
       print(nombre)
    
 
if __name__ == '__main__':
   api = 'https://pokeapi.co/api/v2/pokemon?offset=0&limit=1154'
   destino=r"C:\\Users\diego\\OneDrive\\Escritorio\\Videos descargados"
   url_video=['https://youtu.be/XPDVmBg5DeE','https://youtu.be/B_tTymvDWXk','https://youtu.be/o1z2DfFZBS4','https://youtu.be/cnHsYvAr0EE','https://youtu.be/ZVFFbHXd2Xc' ]
   th1 = threading.Thread(target=descarga, args= [url_video])
   th1.start()
   th2= threading.Thread(target=registro_db, args=[api])
   th2.start()
   x=0
   for x in range(0,50):
     th3 = threading.Thread(target=get_services, args=[x])
     th3.start()
     th3.join()



    