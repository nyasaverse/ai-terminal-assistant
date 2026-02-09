import webbrowser
import datetime
from speech_engine import speak

def respond(command):
    command = command.lower()

    # ---------- BASIC TALK ----------
    if "hello" in command or "hi" in command:
        speak("Hello. Ask me anything, I will try to help you.")

    elif "how are you" in command:
        speak("I am good. More importantly, how are you?")

    # ---------- TIME ----------
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")

    # ---------- OPEN APPS / WEBSITES ----------
    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "netflix" in command:
        speak("Opening Netflix")
        webbrowser.open("https://www.netflix.com")

    elif "spotify" in command:
        speak("Opening Spotify")
        webbrowser.open("https://open.spotify.com")

    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "email" in command or "gmail" in command:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")

    # ---------- TEACHING / QUESTION MODE ----------
    elif "what is" in command or "who is" in command or "how to" in command or "why" in command:
        speak("Let me explain this to you.")
        query = command.replace(" ", "+")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    # ----------  FRIEND MODE ----------
    elif "tired" in command or "thak" in command:
        speak("You are working hard. Take a short break, then continue. You are doing well.")

    elif "motivate" in command:
        speak("Consistency matters more than perfection. Keep going.")

    elif "sad" in command or "low" in command:
        speak("It is okay to feel low sometimes. You are learning and growing.")

    # ---------- EXIT ----------
    elif "bye" in command or "exit" in command or "quit" in command:
        speak("Goodbye. I am always here when you need help.")
        exit()

    # ---------- DEFAULT : LIKE chatgpt TEACHING ----------
    else:
        speak("That is a good question. Let me help you understand.")
        query = command.replace(" ", "+")
        webbrowser.open(f"https://www.google.com/search?q={query}")
