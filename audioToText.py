import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Goul Chy Haja :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("Galti : {}".format(text))
    except:
        print("Mafhemt walo !!")