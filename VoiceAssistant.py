import speech_recognition as sr
import os
import pyttsx3
import pywhatkit as kit
import datetime
import asyncio

class VoiceAssistant:
    """A voice command assistant that can perform various tasks based on voice commands."""

    def __init__(self):
        """Initialize the voice assistant with a text-to-speech engine and a speech recognizer."""
        self.engine = pyttsx3.init() 
        self.engine.setProperty('voice', self.engine.getProperty('voices')[1].id) 
        self.r = sr.Recognizer()

    def text_to_speech(self, text: str) -> None:
        """Convert text to speech and print it on the screen.

        Args:
            text (str): The text to be converted to speech.

        Returns:
            None
        """

        self.engine.say(text) 
        self.engine.runAndWait()
        print(text) 

    def get_speech_input(self, prompt: str) -> str:
        """Get speech input from the microphone and convert it to text.

        Args:
            prompt (str): The prompt to be said before listening to the speech input.

        Returns:
            str: The text converted from the speech input, or None if there was an error.
        """
        with sr.Microphone() as source: # Use the microphone as the source of audio
            self.text_to_speech(prompt) 
            audio_data = self.r.record(source, duration=4) # Record the audio for 4 seconds
            try:
                text = self.r.recognize_google(audio_data) 
                print(text,"\n") 
                return text
            except sr.UnknownValueError:
                self.text_to_speech("SIR.... I COULD NOT UNDERSTAND YOU...") 
            except sr.RequestError: 
                self.text_to_speech("SIR.... I COULD NOT CONNECT TO THE INTERNET...")

    async def execute_command(self, cmd: str) -> bool:
        """Execute a command based on the given text.

        Args:
            cmd (str): The text of the command.

        Returns:
            bool: True if the command was executed successfully, False if the command was to stop the assistant.
        """

        if "WhatsApp" in cmd:
            now = datetime.datetime.now()
            self.text_to_speech("Who do you want to send... Write down the number")
            number = input("write here - ")
            message = self.get_speech_input("what's your message....")
            try:
                await kit.sendwhatmsg(number, message, now.hour, now.minute + 2)
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

    async def run(self) -> None:
        """Run the voice assistant until the user says "rest" or "shutdown".

        Returns:
            None
        """
        agin = True

        while(agin): 
          text = self.get_speech_input("SIR what's your COMMAND....") 

          if text is not None and "friday" in text.lower(): 
              cmd = text.replace("Friday","").replace("friday","").strip()
              agin = await self.execute_command(cmd) 

if __name__ == "__main__":
    assistant = VoiceAssistant() # Create an instance of the voice assistant
    asyncio.run(assistant.run()) # Run the voice assistant
