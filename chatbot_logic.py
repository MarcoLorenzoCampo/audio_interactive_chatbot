from translator import Translator
import openai
import sys
from speaker import Speaker


messages = []

def main():
    chat()
    return


def chat():
    speak_mode = '--speak' in sys.argv
    talk_mode = '--talk' in sys.argv

    while True:
        if talk_mode:
            question = record_voice()
            print(f'>> {question}')
        else:
            question = input('>> ')

        reply = send_to_open_ai(question)

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


if __name__ == '__main__':
    main()