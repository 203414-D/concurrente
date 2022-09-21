
import json
import requests 
import time
import psycopg2 
import concurrent.futures
import threading

threading_local = threading.local()
conection = psycopg2.connect(database="postgres", user="postgres", password="registro12", host="127.0.0.1", port="5432")
def service(url):
     with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_service,url)
        pass

def get_service(url): 
    response = requests.get(url) 
    if response.status_code == 200:
        payload = response.json()
        write_db(payload)


def write_db(payload):
 results = payload.get('results', [])
 if results:
    for pokemon in results:
     name = pokemon['name']
     cursor = conection.cursor()
     sql="INSERT INTO pokemones(nombres) VALUES (%s)"
    map= name
    print(name)
    cursor.execute(sql,(json.dumps(map),))
    conection.commit()
pass


if __name__=="__main__":
    url = ['https://pokeapi.co/api/v2/pokemon?offset=0&limit=1154']
    init_time = time.time()
    service(url)
    end_time = time.time() - init_time
    print(end_time)