from speech_engine import speak
from brain import respond

speak("I am ready. Ask me anything.")

while True:
    command = input("You: ")
    respond(command)
