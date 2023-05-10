import speech_recognition as sr

class Translator:
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        
    def record_and_translate(self, duration):
        with sr.Microphone() as source:
            #print("Please start speaking...")
            audio = self.recognizer.listen(source)
            #print("Translating audio to text...")
            try:
                text = self.recognizer.recognize_google(audio)
                #print("Translated text:", text)
                return(str(text))
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))