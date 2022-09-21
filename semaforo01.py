from threading import Thread, Semaphore
from pytube import YouTube
semaforo = Semaphore(1)


def descarga(vid):
    yt = YouTube(vid)
    video=  yt.streams.filter(file_extension='mp4').order_by('resolution').first()
    video.download(destino)
    print("video descargado en: "+destino)

class Hilo(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        video=id
        self.id=video

    def run(self):
        semaforo.acquire()
        descarga(self.id)
        semaforo.release()


destino=r"C:\\Users\diego\\OneDrive\\Escritorio\\Videos descargados"
threads_semaphore = [Hilo('https://youtu.be/80npsOIuT5U'), Hilo('https://youtu.be/GphzW-OCHRU'), Hilo('https://youtu.be/xS2F8OoCEMc'), Hilo('https://youtu.be/ZVFFbHXd2Xc'),
Hilo('https://youtu.be/aWLWqM_7e9E0'), Hilo('https://youtu.be/LjCiCncxQ48'), Hilo('https://youtu.be/cnHsYvAr0EE'), Hilo('https://youtu.be/ncHsfpkiV4E'), Hilo('https://youtu.be/bTbdwVIvkS8'),
Hilo('https://youtu.be/TnITTT-U3Zs')]
for t in threads_semaphore:
    t.start()

