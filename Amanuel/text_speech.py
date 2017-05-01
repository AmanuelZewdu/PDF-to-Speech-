import pyttsx

class text_speech(object):

    def read_text(self,text):
        self.text= text

        engine = pyttsx.init()
        engine.say(self.text)
        engine.runAndWait()

    def Interupt_Speech(self):
        engine = pyttsx.init()
        engine.stop()

    def change_volume(self):
        engine = pyttsx.init()
        volume = engine.getProperty('volume')
        engine.setProperty('volume', volume-0.25)




