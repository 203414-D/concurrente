import time
from pytube import YouTube
destino=r"C:\\Users\diego\\OneDrive\\Escritorio\\Videos descargados"
url=['https://youtu.be/XPDVmBg5DeE','https://youtu.be/B_tTymvDWXk','https://youtu.be/o1z2DfFZBS4','https://youtu.be/cnHsYvAr0EE','https://youtu.be/ZVFFbHXd2Xc' ]

def streams():
  for x in url:
     yt = YouTube(x)
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
    init_time = time.time()
    streams()
    end_time = time.time() - init_time
    print(end_time)