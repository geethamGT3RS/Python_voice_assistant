import pyttsx3
import datetime                                  
import speech_recognition as sr                   
import wikipedia                                  
import webbrowser                                 
import os.path                            

 # sapi5 is an API and the technology for voice recognition and synthesis provided by Microsoft
                          
engine = pyttsx3.init('sapi5')                   
voices = engine.getProperty('voices')             
engine.setProperty('voice',voices[1].id)          



def speak(audio):                              
    engine.say(audio)
    engine.runAndWait()      
    
def talk():                                 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning')

    elif hour>12 and hour<18:
        speak('Good Afternoon')

    else:
        speak('Good Evening')

    speak('Hello, how may I help you')


def VoiceInput():                            
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 2
        audio = r.listen(source)
    try:                                         
        print('Recognizing...')
        query = r.recognize_google(audio,language = 'en-in') 
        print(f'User said: {query}\n')

    except Exception as e :
        print('I didnt catch that...')        
        return 'None'  
    return query


if __name__ == '__main__' :                 
    wishme()
    while True:
        query = VoiceInput()().lower() 
     
        if 'wikipedia' in query :
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences = 5)
            print(results)
            speak(results)

        elif 'open youtube' in query :
            webbrowser.open('youtube.com')

        elif 'open google' in query :
            webbrowser.open('google.com')

        elif 'time' in query :
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'the time is {strtime}')

        elif 'close' in query:
            speak('okay, see you soon')
            quit()
