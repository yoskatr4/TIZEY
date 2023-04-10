
import openai_secret_manager
import openai
import speech_recognition as sr
from gtts import gTTS
import os
import pyttsx3

openai.api_key = "APİ_KEY"
r = sr.Recognizer()

engine = pyttsx3.init()

def speak(text):
    tts = gTTS(text=text, lang='tr')
    tts.save("sonyanıt.mp3")
    os.system("mpg321 sonyanıt.mp3")
    engine.say(text)
    engine.runAndWait()

def ask_gpt(question):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{question}\nA:",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    answer = response.choices[0].text.strip()
    return answer

while True:
    with sr.Microphone() as source:
        print("Soru sorun...")
        audio = r.listen(source)

    try:
        question = r.recognize_google(audio, language="tr-TR")
        print(f"Soru: {question}")
        answer = ask_gpt(question)
        print(f"Yanıt: {answer}")
        speak(answer)
    except sr.UnknownValueError:
        print("Ne söylediğinizi anlayamadım, lütfen tekrar deneyin.")
    except sr.RequestError as e:
        print(f"Ses algılama hizmeti çalışmıyor: {e}")
