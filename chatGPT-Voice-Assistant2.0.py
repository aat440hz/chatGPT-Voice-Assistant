import openai
import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Your OpenAI API Key
openai.api_key = 'your-api-key-here'

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            return text
        except:
            return "Sorry, I did not get that."

def speak(text):
    engine.say(text)
    engine.runAndWait()

def ask_gpt_chat(question):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo-1106",
      messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": question},
      ]
    )
    return response.choices[0].message['content']

if __name__ == "__main__":
    while True:
        print("Say something...")
        query = listen()
        if "exit" in query.lower():
            break

        response = ask_gpt_chat(query)
        print("GPT-3.5:", response)
        speak(response)
