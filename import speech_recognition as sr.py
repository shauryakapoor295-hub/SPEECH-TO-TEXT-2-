import speech_recognition as sr
import sounddevice as sd
import numpy as np

# 1. Initialize recognizer
recognizer = sr.Recognizer()

# 2. Recording settings
sample_rate = 16000  # 16,000 samples per second
duration = 7         # Record for 7 seconds

print("Canteen Voice Ordering System")
print("Speak your food order...\n")

# 3. Record voice using microphone
audio = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype='int16'
)

sd.wait()  # Wait until recording is complete

print("Recording completed.")
print("Transcribing...")

# 4. Convert audio to text using Google Speech Recognition
audio_data = sr.AudioData(audio.tobytes(), sample_rate, 2)

try:
    text = recognizer.recognize_google(
        audio_data,
        language="en-IN"
    )

    print("\n----- CANTEEN ORDER -----")
    print("Your Order:", text)

except sr.UnknownValueError:
    print("Could not understand your order.")

except sr.RequestError as e:
    print("Google service error:", e)
