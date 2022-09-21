import time
from pytube import YouTube
import concurrent.futures
import threading

threading_local = threading.local()

def servicio(url_video):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(streams,url_video)

def streams(url_video):
    yt = YouTube(url_video)
    descarga(yt)
 

def descarga(yt):
    ## -- alta resolution
  ##  video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

    ## -- baja resolution 
    video=  yt.streams.filter(file_extension='mp4').order_by('resolution').first()
    video.download(destino)
    print("descargado en: "+destino)
    pass

if __name__=="__main__":
    destino=r"C:\\Users\diego\\OneDrive\\Escritorio\\Videos descargados"
    url_video=['https://youtu.be/XPDVmBg5DeE','https://youtu.be/B_tTymvDWXk','https://youtu.be/o1z2DfFZBS4','https://youtu.be/cnHsYvAr0EE','https://youtu.be/ZVFFbHXd2Xc' ]
    init_time = time.time()
    servicio(url_video)
    end_time = time.time() - init_time
    print(end_time)