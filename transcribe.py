# Import the necessary libraries
import speech_recognition as sr

# Initialize the speech recognizer
r = sr.Recognizer()

# Read the audio file
with sr.AudioFile('emma.wav') as source:
    audio_data = r.record(source)

# Transcribe the audio data to texttr
text = r.recognize_google(audio_data)

# Print the transcribed text
print(text)
