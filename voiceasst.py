import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
contacts = {
    'akshay': 'akshaysrkondu@gmail.com',
    'abhi': 'konduabhisree@gmail.com',
    'akhila': 'janumpallyakhila1207@gmail.com'
}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        print("Good Morning!!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
        print("Good Afternoon!!")
    else:
        speak("Good Evening!")
        print("Good Evening!!")

    speak("I am Chitti AI voice assistant.")
    print("I am Chitti AI voice assistant.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Please try saying again...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abhikondu597@gmail.com', 'qkup xhjq cola cscp')  # App Password
    server.sendmail('abhikondu597@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    print("Following are the activities I can do:")
    speak("Following are the activities I can do:")
    print("Searching in Wikipedia")
    speak("Searching in Wikipedia")
    print("Opening YouTube")
    speak("Opening YouTube")
    print("Opening Google")
    speak("Opening Google")
    print("Playing music")
    speak("Playing music")
    print("Displaying current time")
    speak("Displaying current time")
    print("Sending mails")
    speak("Sending mails")
    print("How can I help you??")
    speak("Now,Tell me how can I help you")

    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'search' in query:
            speak('Searching Wikipedia...')
            query = query.replace("search", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('http://www.youtube.com')
        elif 'open google' in query:
            webbrowser.open('http://www.google.com')
        elif 'open mail' in query:
            webbrowser.open('http://www.gmail.com')
        elif 'play music' in query:
            music_dir = 'D://python project//songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            print(f"The time is {strTime}")

        elif 'send mail to' in query or 'send email to' in query:
            try:
                to = None
                for name in contacts:
                    if name in query:
                        to = contacts[name]
                        break
                if to is None:
                    speak("I couldn't find a contact by that name.")
                    print("I couldn't find a contact by that name.")
                    continue
                speak("What should I send?")
                content = takeCommand()
                if content.lower() == "none":
                    speak("I couldn't understand the content. Please try again.")
                    continue
                sendEmail(to, content)
                print(f"Sent email to: {to} successfully!!")
                speak(f"Email has been sent to {name} successfully!")
            except Exception as e:
                print(e)
                speak("Sorry my friend... I am not able to send this email.")
                print("Sorry my friend... I am not able to send this email.")
        elif 'my work is done' in query or 'thank you' in query or 'exit' in query or 'terminate' in query:
            speak("You're welcome! Have a great day!")
            print("You're welcome! Have a great day!")
            break
    exit()
    # Add a comment
    