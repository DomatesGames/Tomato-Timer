  
import time
import vlc
author = "DomatesGames from Github"
saat = int(input("Kaç saat? "))
saat = saat*60*60
dakika = int(input("Kaç dakika? "))
dakika = dakika*60
saniye = int(input("Kaç saniye? "))
saniye = saniye
time.sleep(saat + dakika + saniye)
print("Süre doldu!")
p = vlc.MediaPlayer(r"C:\Users\W7\Desktop\ses.mp3")
p.play()
