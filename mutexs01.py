import threading
from pytube import YouTube


mutex = threading.Lock()
def descarga(vid):
    yt = YouTube(vid)
    video=  yt.streams.filter(file_extension='mp4').order_by('resolution').first()
    video.download(destino)
    print("video descargado en: "+destino)

class Hilo(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        video=id
        self.id=video


    def run(self):
        mutex.acquire()
        descarga(self.id)
        mutex.release()

destino=r"C:\\Users\diego\\OneDrive\\Escritorio\\Videos descargados"
Hilos = [Hilo('https://youtu.be/80npsOIuT5U'), Hilo('https://youtu.be/GphzW-OCHRU'), Hilo('https://youtu.be/xS2F8OoCEMc'), Hilo('https://youtu.be/ZVFFbHXd2Xc'),
Hilo('https://youtu.be/aWLWqM_7e9E0'), Hilo('https://youtu.be/LjCiCncxQ48'), Hilo('https://youtu.be/cnHsYvAr0EE'), Hilo('https://youtu.be/ncHsfpkiV4E'), Hilo('https://youtu.be/bTbdwVIvkS8'),
Hilo('https://youtu.be/TnITTT-U3Zs')]
for h in Hilos:
    h.start()