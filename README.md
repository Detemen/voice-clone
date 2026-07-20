# voice-clone

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![ElevenLabs](https://img.shields.io/badge/ElevenLabs-voice%20cloning-000000)
![TTS](https://img.shields.io/badge/F5--TTS%20%7C%20Edge--TTS-comparison-orange)

R&D scripts comparing voice-cloning/TTS approaches for quality and latency — ElevenLabs, F5-TTS and Edge-TTS side by side.

## Scripts

- `test_eleven.py` — ElevenLabs voice cloning (multilingual v2 model)
- `test_f5.py` — F5-TTS local inference
- `test_edge_emotion.py` — Edge-TTS with emotion/style variation
- `test_voice.py` — quick comparison harness
- `transcribe_ref.py` — transcribes a reference sample for voice matching
- `generate_audio.py` — batch generation entrypoint

## Stack

Python, ElevenLabs API, F5-TTS, Edge-TTS.

## Running

```bash
export ELEVENLABS_API_KEY=sk_...
python test_eleven.py
```
