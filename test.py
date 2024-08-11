from gtts import gTTS
from mutagen.mp3 import MP3
import translators as ts
import os
import time



def TTS(Text,Lang="en",Slow=False):
    audio = gTTS(text = ts.translate_text(Text,'bing','auto',Lang), lang=Lang,slow= Slow)
    filename: str = "tts.mp3"
    audio.save(filename)
    audioFile = MP3(filename)
    length = audioFile.info.length
    os.system("start "+filename)
    time.sleep(length)
    os.remove(filename)

def minecraftSessions(a,b):
    x = 1

    ap = a
    c = 0
    ap/=x
    while ap >= 60:
        ap -= 60
        c += 1

    while c > 3:
        x += 1
        ap = a
        c = 0
        ap/=x
        while ap >= 60:
            ap -= 60
            c += 1
    return "you can split it over "+str(x)+" sessions of "+str(c)+" hours and "+str(int(ap))+" minutes each"

def MinecraftDays(days):
    x = 0
    a = days
    days *= 20
    while days >= 60:
        days -= 60
        x += 1
    b = x
    c = 0
    while b >= 24:
        b-=24
        c += 1

    result: str = str(a)+" days in minecraft is " + str(x) +" hours and "+ str(days) + " minutes in real life time."
    if c!=0:
        if c == 1:
            result += " In other words: " + str(c) + " day"
        else:
            result += " In other words: " + str(c) + " days"

    if b!=0:
        if b == 1:
            result += ", "+str(b)+" hour"
        else:
            result += ", "+str(b)+" hours"

    if c !=0:
        result += " and "+str(days)+" minutes"
    separate:str = ""
    if x > 3:
        separate = "but "+minecraftSessions(x*60+days,3)
    result += separate
    print(result)
    TTS(result,"en",False)



