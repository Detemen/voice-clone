import os
os.environ["COQUI_TOS_AGREED"] = "1"

from TTS.api import TTS

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

tts.tts_to_file(
    text="Сегодня в мире искусственного интеллекта сразу несколько важных событий. Разбираем всё по порядку.",
    speaker_wav="/Users/artemcvetkov/Desktop/Новий запис 4.m4a",
    language="ru",
    file_path="/Users/artemcvetkov/Desktop/test_output.wav"
)

print("Готово! Файл збережено на робочий стіл: test_output.wav")
