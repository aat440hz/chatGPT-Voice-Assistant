import os
from openai import OpenAI

client = OpenAI(api_key='your-open-api-key')
from dotenv import load_dotenv
import time
import speech_recognition as sr
import pyttsx3
import pygame

language = 'en'
load_dotenv()
model = 'gpt-3.5-turbo'

# Set up the speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Find and set the English voice if available
english_voice_id = None
for voice in engine.getProperty('voices'):
    if "english" in voice.name.lower():
        english_voice_id = voice.id
        break

if english_voice_id is not None:
    engine.setProperty('voice', english_voice_id)
    print("English voice set.")
else:
    print("No English voice found. The default voice will be used.")

# Load the tone sound file
pygame.mixer.init()
tone_file = "/home/user/chatGPT-Voice-Assistant/tone.wav"
pygame.mixer.music.load(tone_file)

# Function to play the tone
def play_tone():
    pygame.mixer.music.play()

# Function to listen for the wake word "meatball"
def listen_for_wake_word(source):
    print("Listening for 'Meatball'...")

    while True:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            if "meatball" in text.lower():
                print("Wake word detected.")
                play_tone()
                return True
        except sr.UnknownValueError:
            pass

# Function to listen and respond with OpenAI API
def listen_and_respond(source):
    print("Listening...")

    # Read the previous interaction from transcript.txt if it exists
    if os.path.exists("transcript.txt"):
        with open("transcript.txt", "r") as file:
            transcript = file.read()
    else:
        transcript = ""

    while True:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="en")  # Set the language to English
            print(f"You said: {text}")
            if not text:
                continue

            # Append the current user input to the transcript
            transcript += f"You: {text}\n"

            # Send the entire conversation to the OpenAI API
            response = client.chat.completions.create(model=model, messages=[{"role": "system", "content": transcript}, {"role": "user", "content": text}])
            response_text = response.choices[0].message.content
            print(response_text)

            # Append the response to the transcript
            transcript += f"Assistant: {response_text}\n"

            # Save the updated transcript to transcript.txt
            with open("transcript.txt", "w") as file:
                file.write(transcript)

            # Speak the response with English language
            engine.say(response_text)
            engine.runAndWait()

            play_tone()
            return
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            engine.say(f"Could not request results; {e}")
            engine.runAndWait()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    while True:
        if listen_for_wake_word(source):
            listen_and_respond(source)

