import speech_recognition as sr
import pyttsx3
from google_trans_new import google_translator

#initialize the recognizer
r = sr.Recognizer()
translator = google_translator()
engine = pyttsx3.init()

#use microphone as source for input
while True :
    with sr.Microphone(device_index=2) as source:
        print("Clearing the background noice..")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening")
        voice = r.listen(source,timeout=5,phrase_time_limit=5)
        print("Done recording")
    try:
        print("Recognizing")
        result = r.recognize_google(voice, language='en')
        print(result)
    except Exception as ex:
        print(ex)
        
#Translation. It doesn't work due to httpError.
    def trans():
        lanInput = input("Type the language code you want to translate")
        translator = google_translator()
        translate_text = translator.translate(str(result), lang_tgt=str(lanInput))
        print(translate_text)
        engine.say(str(translate_text))
        engine.runAndWait()


