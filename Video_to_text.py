"""
Video_to_text
"""

#!/usr/bin/env python
# coding: utf-8

# In[3]:


import moviepy.editor as mp
import speech_recognition as sr

def extract_audio(video_path, audio_path):
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language= "en-US")  # Change to 'en-US' for English
        return text
    except sr.UnknownValueError:
        return "No se pudo reconocer el audio"
    except sr.RequestError as e:
        return f"No se pudo completar la solicitud: {e}"

# Rutas de archivos
video_path = r"C:\Users\HP\Videos\Movavi Screen Recorder\BUSINESS MODEL CANVAS\1.- SEGMENTO DE CLIENTES.mp4"
audio_path = 'audio.wav'

# Extraer audio del video
extract_audio(video_path, audio_path)

# Transcribir el audio
texto_transcrito = transcribe_audio(audio_path)
print("Texto transcrito:")
print(texto_transcrito)


# In[ ]:





# In[ ]:






if __name__ == "__main__":
    pass
