import pyttsx3

class Speaker:
    def __init__(self, rate=170, volume=1.0, voice=None):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
        if voice is not None:
            voices = self.engine.getProperty('voices')
            for v in voices:
                if voice.lower() in v.name.lower():
                    self.engine.setProperty('voice', v.id)
                    break

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()