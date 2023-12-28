# Voice Command Assistant

## Description
This project is a voice command assistant that can perform various tasks such as sending WhatsApp messages, opening Paint, and shutting down the system based on voice commands. It uses the `speech_recognition`, `pyttsx3`, and `pywhatkit` libraries.

## Getting Started

### Dependencies
- Python 3.x
- speech_recognition
- pyttsx3
- pywhatkit
- datetime

You can install the necessary libraries using pip:
```bash
pip install speechRecognition pyttsx3 pywhatkit datetime
```

### Executing program
To run the program, navigate to the directory containing the script and use the following command:
```bash
python voice_command_assistant.py
```
Wait for the assistant to say “SIR what’s your COMMAND…” and then speak your command into the microphone. Make sure you have a working internet connection and a clear voice.

#### Some of the commands that you can use are:

- “Friday paint” to open Paint application.
- “Friday shutdown” to shutdown the system.
- “Friday rest” to stop the assistant.

  
You can also use other commands that are not predefined, such as opening a website or a file. The assistant will try to execute them using the os module.

## Help
If you encounter any problems or issues, feel free to open an issue on this GitHub repository.

## Version History
* 0.1
    * Initial Release

## License
This project is licensed under the MIT License - see the LICENSE.md file for details

