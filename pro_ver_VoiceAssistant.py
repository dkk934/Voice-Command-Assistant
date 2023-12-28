import speech_recognition as sr
import os
import pyttsx3
import pywhatkit as kit
import datetime
# import threading
import asyncio

class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', self.engine.getProperty('voices')[1].id)
        self.r = sr.Recognizer()

    def text_to_speech(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
        print(text)

    def get_speech_input(self, prompt):
        with sr.Microphone() as source:
            self.text_to_speech(prompt)
            audio_data = self.r.record(source, duration=3)
            try:
                text = self.r.recognize_google(audio_data)
                print(text,"\n")
                return text
            except sr.UnknownValueError:
                self.text_to_speech("SIR.... I COULD NOT UNDERSTAND YOU...")
            except sr.RequestError:
                self.text_to_speech("SIR.... I COULD NOT CONNECT TO THE INTERNET...")

    async def execute_command(self, cmd):
        if "WhatsApp" in cmd:
            now = datetime.datetime.now()
            message = self.get_speech_input("what's your message....")
            try:
                await kit.sendwhatmsg("+917011290087", message, now.hour, now.minute + 2)
            except Exception as e:
                print(f"Failed to send message: {e}")

        elif "paint" in cmd:
            os.system("start C:\\Users\\karishma\\OneDrive\\Desktop\\Paint.lnk")
            self.text_to_speech("SIR.... HERE WHAT YOU..ASKED...")

        elif "shutdown" in cmd:
            os.system("shutdown /s")
            self.text_to_speech("SIR SYSTEM GOING TO SHUTDOWN IN LESS THAN MINUTE ....")
            return False

        elif "rest" in cmd:
            self.text_to_speech("GOOD DAY SIR....")
            return False

        else:
            os.system(cmd)
        return True

    async def run(self):
        agin = True

        while(agin):
          text = self.get_speech_input("SIR what's your COMMAND....")

          if text is not None and "friday" in text.lower():
              cmd = text.replace("Friday","").replace("friday","").strip()
              agin = await self.execute_command(cmd)

if __name__ == "__main__":
    assistant = VoiceAssistant()
    asyncio.run(assistant.run())
