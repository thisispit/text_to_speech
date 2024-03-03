import os

if __name__ == '__main__':
    print("Welcome to text to speech")
    
    while True:
        x = input("Type and press enter to speak: ")

        if x=="q" and "Q":
            break
        
        command = f"powershell -Command \"Add-Type -AssemblyName System.speech; $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; $speak.Speak('{x}')\""
        
        os.system(command)