import speech_recognition as sr
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the speech recognizer
r = sr.Recognizer()
print(sr.Microphone())
# Set the microphone as the audio source
with sr.Microphone() as source:
    print("Say something!")
    while True:
        print("|||")
        # Listen for audio input

        audio = r.listen(source)
        # Convert audio to text
        try:

            text = r.recognize_google(audio)
            print("You said: ", text)

            # # Convert text to speech output
            engine.say("Прувет")
            engine.runAndWait()

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
