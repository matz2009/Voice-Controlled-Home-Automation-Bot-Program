import speech_recognition as sr

def get_voice_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak your command...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        print("Could not understand")
        return ""
