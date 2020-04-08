from pygame import mixer
mixer.init()
mixer.music.load('yo.mp3')
mixer.music.play()
input('Digite qualquer coisa para parar a música?')