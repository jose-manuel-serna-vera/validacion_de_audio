import fitz
import json
import pytesseract
from PIL import Image
import time
import os
from pydub import AudioSegment
from os import path
import speech_recognition as sr

r = sr.Recognizer()
#   python -m pip install --upgrade pip
#   python -m pip install --upgrade pymupdf


############ PDF - PNG
def process(file_dir,file_name):
    with sr.AudioFile(file_dir+"/"+file_name) as recurso:
     audioss= r.listen(recurso)
    try:
        print("leyendo fichero de audio")
        text = r.recognize_google(audioss, language='es-ES')
        time.sleep(0.5)
        text = str(text)            
    except:
        print("lo siento no entendi")


    # convertir con nombre
    # print(text)
    numbers = [int(temp)for temp in text.split() if temp.isdigit()]
    if numbers != []:            
        file_oldname = os.path.join(file_dir, "{}".format(file_name))
        numeroFinal =listToString(numbers)
        numeroFinal = numeroFinal.replace(" ","")
        file_newname_newfile = os.path.join(file_dir, "{}.wav".format(numeroFinal))
        os.rename(file_oldname, file_newname_newfile)
        print("cambio de nombre exitosamente")  
        print(numeroFinal)
    else:
        print("palabra no encontrada")
        print(numbers)
        os.remove(os.path.join(file_dir, file_name))
    
    return text
    
# Function to convert  
def listToString(s): 
    # traverse in the string  
    listToStr = ' '.join([str(elem) for elem in s])
    # return string  
    return listToStr 