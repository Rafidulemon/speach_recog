import speech_recognition as sr
import pyttsx3
from google_trans_new import google_translator
from gtts import gTTS
from playsound import playsound
import os

# initialize the recognizer
r = sr.Recognizer()
translator = google_translator()

#use microphone as source for input
while True :
    with sr.Microphone() as source:
        print("Listening...")
        voice = r.listen(source)

        try:
            MyText = r.recognize_google(voice)
            MyText = MyText.lower()
            print(MyText)
            if(MyText == "exit"):
                break

        except sr.UnknownValueError:
            print("Couldn't understand")
        except sr.RequestError:
            print("Couldn't request result from google")


        translated_text = translator.translate(MyText, lang_tgt='ja')
        print(translated_text)

        voice = gTTS(translated_text, lang='ja')
        voice.save("MyVoice.mp3")
        playsound("MyVoice.mp3")
        os.remove("MyVoice.mp3")

