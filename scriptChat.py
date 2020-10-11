import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something..")
    audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print(f"You said: {r.recognize_google(audio)}")
    except:
        print("Sorry could not recognize your voice")
