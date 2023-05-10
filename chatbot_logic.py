from translator import Translator
import openai
import sys
from speaker import Speaker
import os

messages = []

def get_messages():
    return messages

def chat():
    speak_mode = '--speak' in sys.argv
    record_mode = '--record' in sys.argv
    question = ''    

    if record_mode:
        question = record_voice()
        print(f'>> {question}')
    else:
        question = input('>> ')

    reply = send_to_open_ai(question)[-1]

    print(f'ChatGPT said: {reply}')

    if speak_mode:
        speak(reply)


# This function simply allows to send a TEXT message to ChatGpt and print the response.
def send_to_open_ai(question):
    
    messages.append({"role":"user", "content": question})

    response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=messages,
            temperature=0.2
        )

    reply = response["choices"][0]['message']['content']
    messages.append({"role":"assistant", "content":reply})

    return reply

def speak(answer):
    Speaker().speak(answer) 

# Function to record, for example for 3 seconds
def record_voice():
    translator = Translator()
    return translator.record_and_translate(duration = 10)

def set_key():
    openai.api_key = os.environ.get("OPENAI_API_KEY")

def set_speak_mode():
    if '--speak' in sys.argv:
        sys.argv.remove('--speak')
        return 'Talking mode inactive'
    else:
        sys.argv.append('--speak')
        return 'Talking mode active'

def set_record_mode():
    if '--record' in sys.argv:
        sys.argv.remove('--record')
        return 'Recording mode inactive'
    else:
        sys.argv.append('--record')
        return 'Recording mode active'