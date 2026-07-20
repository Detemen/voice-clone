import asyncio
import edge_tts

# Текст з SSML розміткою — паузи, темп, наголос
ssml = """
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
       xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="ru-RU">
  <voice name="ru-RU-DmitryNeural">
    <prosody rate="+10%" pitch="+2%">
      Искусственный интеллект меняет всё вокруг нас
    </prosody>
    <break time="300ms"/>
    <prosody rate="+20%" pitch="+5%" volume="+20%">
      быстрее, чем мы успеваем это осознать.
    </prosody>
    <break time="500ms"/>
    <prosody rate="0%" pitch="0%">
      Сегодня разберём три главных инструмента,
    </prosody>
    <break time="200ms"/>
    <prosody rate="+5%" pitch="+3%">
      которые реально сэкономят ваше время.
    </prosody>
  </voice>
</speak>
"""

async def generate():
    communicate = edge_tts.Communicate(ssml, voice="ru-RU-DmitryNeural")
    await communicate.save("/Users/artemcvetkov/Desktop/edge_emotion.mp3")
    print("Готово → edge_emotion.mp3")

asyncio.run(generate())
