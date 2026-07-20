import os
import sys

import requests

API_KEY = os.environ.get("ELEVENLABS_API_KEY", "")
if not API_KEY:
    print("Set ELEVENLABS_API_KEY env var first", file=sys.stderr)
    sys.exit(1)

text = "Искусственный интеллект меняет всё вокруг нас быстрее, чем мы успеваем это осознать. Сегодня разберём три главных инструмента, которые реально сэкономят ваше время. Поехали!"

voices = {
    "voice_1": "LHi3adMlU7AICv8Yxpmm",
    "voice_2": "bqbHGIIO5oETYIqhWmfk",
    "voice_3": "TtRFBnwQdH1k01vR0hMz",
}

for name, voice_id in voices.items():
    # Дізнаємось назву голосу
    info = requests.get(
        f"https://api.elevenlabs.io/v1/voices/{voice_id}",
        headers={"xi-api-key": API_KEY}
    ).json()
    voice_name = info.get("name", name)

    r = requests.post(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
        headers={"xi-api-key": API_KEY, "Content-Type": "application/json"},
        json={
            "text": text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.4,
                "similarity_boost": 0.75,
                "style": 0.6,
                "use_speaker_boost": True
            }
        }
    )
    path = f"./{name}_{voice_name}.mp3"
    with open(path, "wb") as f:
        f.write(r.content)
    print(f"Готово → {name}_{voice_name}.mp3")
