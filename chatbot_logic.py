from translator import Translator
import openai
from speaker import Speaker
import os
import sys

class Chatbot:
    
    def __init__(self):
        self.messages = []

    def get_messages(self):
        return self.messages
    
    def speak(self, answer):
        Speaker().speak(answer)

    def send_to_open_ai(self, question):

        speak_mode = '--speak' in sys.argv
        record_mode = '--record' in sys.argv

        self.messages.append({"role": "user", "content": question})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
            temperature=0.2
        )

        reply = response["choices"][0]['message']['content']
        self.messages.append({"role": "assistant", "content": reply})

        if(speak_mode):
            self.speak(reply)

        return reply

    def record_voice(self):
        translator = Translator()
        return translator.record_and_translate(duration=10)

    @staticmethod
    def set_key():
        openai.api_key = os.environ.get("OPENAI_API_KEY")

    @staticmethod
    def set_speak_mode():
        if '--speak' in sys.argv:
            sys.argv.remove('--speak')
            return 'Talking mode inactive'
        else:
            sys.argv.append('--speak')
            return 'Talking mode active'

    @staticmethod
    def set_record_mode():
        if '--record' in sys.argv:
            sys.argv.remove('--record')
            return 'Recording mode inactive'
        else:
            sys.argv.append('--record')
            return 'Recording mode active'
