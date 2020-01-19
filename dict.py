#!/usr/bin/env python3

import pycurl
from io import BytesIO
import translate
from bs4 import BeautifulSoup
from requests import get
from inscriptis import get_text
from sys import argv
from os import popen
from google_speech import Speech
from termcolor import colored
from threading import Thread





# get input words
word = str(argv[1])

# get size terminal
rows, columns = popen('stty size', 'r').read().split()


def Url_Requests():
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, 'https://www.vocabulary.com/dictionary/'+word)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    body = buffer.getvalue()
    global URL
    URL = body.decode('iso-8859-1')

# voice word
def voice_word():   
    Voice = word
    lang = "en"
    speech = Speech(Voice, lang)
    speech.play()

# search in page get text
def search_in_page():
    soup = BeautifulSoup(URL, "lxml")
    Data_search_1 = soup.find("p", class_="short")
    Data_search_2 = soup.find("p", class_="long")
    get_text_1 = get_text(str(Data_search_1))
    get_text_2 = get_text(str(Data_search_2))
    word_align = word.center(int(columns))
    text_ir = "-------------- < Translate IR > ---------------"
    end_command = "-----------------------------------------------------------"
    end_command = end_command.center(int(columns))
    msg_x = text_ir.center(int(columns))
    print( colored(get_text_1, "green"),"\n\n",    colored(get_text_2, "green"))
    print("\n\n",colored(msg_x, "red"),"\n\n")
    print(colored(word_align,"green"), "\n")
    print(colored(end_command,"red"))


# Translate_ir word
def Translate_ir():
    translator = translate.Translator("fa") 
    data_1 = translator.translate(word)
    data_1_fix = data_1.center(int(columns))  
    print(colored(data_1_fix,"green"),"\n\n")


# func main run 
def main():
    t0 = Thread(target=Url_Requests)
    t = Thread(target=voice_word)
    t2 = Thread(target=search_in_page)
    t3 = Thread(target=Translate_ir)
    t0.start()
    t0.join()
    t.start()
    t2.start()
    t3.start()
    t3.join()
    t.join()
    t2.join()


if __name__ == '__main__':
    main()
        