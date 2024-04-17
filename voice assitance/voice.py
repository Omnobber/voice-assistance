import speech_recognition as sr
import pyttsx3
import datetime
from googlesearch import search

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak the response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for voice input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an error recognizing your voice.")
        return ""

# Function to get the current date and time
def get_date_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    current_date = now.strftime("%A, %B %d, %Y")
    return f"The current time is {current_time} and today is {current_date}."

# Function to search the web using Google
def search_web(query):
    speak(f"Searching the web for {query}")
    for j in search(query, tld="com", num=1, stop=1, pause=2):
        speak("Here's what I found on the web.")
        speak(j)

# Function to get summary from Wikipedia
def get_wikipedia_summary(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia, " + summary)
    except wikipedia.exceptions.PageError:
        speak("Sorry, I couldn't find any information on that topic.")
    except wikipedia.exceptions.DisambiguationError:
        speak("Sorry, there are multiple matching results. Please be more specific.")
    except wikipedia.exceptions.HTTPTimeoutError:
        speak("Sorry, there was a timeout while accessing Wikipedia.")

# Main loop
if __name__ == "__main__":
    speak("Hello! How can I assist you today?")

    while True:
        query = listen().lower()

        if "hello" in query:
            speak("Hello! How can I assist you?")
        elif "what is your name" in query:
            speak("My name is Assistant.")
        elif "time" in query:
            speak(get_date_time())
        elif "search" in query:
            query = query.replace("search", "")
            search_web(query)
        elif "summary" in query:
            query = query.replace("summary", "")
            get_wikipedia_summary(query)
        elif "goodbye" in query:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I'm not sure how to help with that.")
