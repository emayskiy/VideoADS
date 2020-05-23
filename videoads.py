'''
Created on 31.03.2016

Скрипт добавления рекламного ролика в фильмы для показа в торговом зале

Для работы:
1. Устанавливаем на компьютере python3
2. Ставим дополнительные пакеты: sudo pip3 install moviepy pillow
3. Меняем настройки скрипта и запускаем его 

@author: emayskiy
'''
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

#Настройки скрипта по умолчанию
srcdir=r"C:\\VIDEO\\IN\\"
dstdir=r"C:\\VIDEO\\OUT\\"
promofile=r"C:\\VIDEO\\promo.mp4"
promointerval=600

clip_ads = VideoFileClip(promofile)
files = os.listdir(srcdir)
for inputfile in files:
    print("Current file: "+srcdir+inputfile)
    cp=0
    final_clip=""
    clip_in = VideoFileClip(srcdir+inputfile)
    if (clip_in.w!=1920 | clip_in.h!=1080):
            clip_in = clip_in.resize((1920,1080))
    while cp<clip_in.end:
        if final_clip=="":
            final_clip=concatenate_videoclips([clip_in.subclip(cp, min(cp+promointerval,clip_in.end)),clip_ads])
        else:
            final_clip=concatenate_videoclips([final_clip,clip_in.subclip(cp, min(cp+promointerval,clip_in.end)),clip_ads])
        cp+=promointerval
    # Записываем итоговый файл
    final_clip.fps=24
    final_clip.write_videofile(dstdir+"e_"+os.path.splitext(inputfile)[0]+".mp4")
