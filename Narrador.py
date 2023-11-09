from gtts import gTTS
import moviepy.editor as mp
import os

_NOMBRE_FICHERO_TEMPORAL = 'temp_audio.mp3'

def audio(text):
    # Convertir el texto a voz (text-to-speech)
    tts = gTTS(text, lang='es')  # Puedes cambiar 'es' por el código del idioma deseado
    tts.save(_NOMBRE_FICHERO_TEMPORAL)
        
    # Cargar el audio generado
    return mp.AudioFileClip(_NOMBRE_FICHERO_TEMPORAL)

def borrar_temp():
    os.borrar(_NOMBRE_FICHERO_TEMPORAL)

if __name__ == "__main__":
    print("No hago nada")
    audio("No me voy a ver b******! ")