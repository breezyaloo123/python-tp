#this library allows us to reconize our voice
import speech_recognition as sr
#this method allows the recognition
r = sr.Recognizer()
#this method take the Microphone as the source
with sr.Microphone() as source:
    print("Tell Anything: ")
    #Now we listen to the source
    audio = r.listen(source)
    #we have a try except loop in order to avoid Exception
    try:
        #we translate the audio into text by the method recognize_google()
        text =  r.recognize_google(audio)
        print("You said: {}".format(text))
    except:
        print("Sorry could not recognize your voice")