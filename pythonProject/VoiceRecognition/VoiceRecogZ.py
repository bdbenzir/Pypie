import speech_recognition as sr

get = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print('Hang on!')
        print('Listening..')
        voice = get.listen(source)
        command = get.recognize_google(voice)
        print(command)

except:
    pass