import asyncio
import edge_tts

script = [
    ("hook",    "Siri мертва. Apple только что заплатила Google миллиард долларов, чтобы признать это официально."),
    ("context", "На WWDC 2026 Apple представила нового Siri. Внутри — модель Gemini на 1,2 триллиона параметров. Лицензия — миллиард долларов в год."),
    ("detail",  "Но вот что интересно. Пользователи смогут сами выбрать мозг для своего iPhone — ChatGPT, Gemini или Claude. Это первый раз в истории Apple, когда они отдают контроль над ключевой функцией пользователю. И это финальный WWDC для Тима Кука."),
    ("outro",   "Что это значит? AI-война переехала прямо в твой карман. И теперь Google живёт внутри каждого нового iPhone."),
    ("cta",     "Подписывайся — каждый день главное из мира AI за минуту."),
]

async def generate():
    full_text = " ".join([text for _, text in script])
    communicate = edge_tts.Communicate(full_text, voice="ru-RU-DmitryNeural", rate="+5%", pitch="+2Hz")
    path = "/Users/artemcvetkov/Desktop/video_audio.mp3"
    await communicate.save(path)
    print(f"Аудіо збережено → {path}")

asyncio.run(generate())
