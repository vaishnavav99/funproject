from gtts import gTTS 
import os 
mytext = input("sentence\t")
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
d = input("FILE Name\t")
d=d+'.mp3'
myobj.save(d)
