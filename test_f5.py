import subprocess
import os

ref_audio = "/Users/artemcvetkov/Desktop/ref_tg_10s.wav"
ref_text = "У меня был в игре старый аккаунт, наверное, из класса. Данюш, в каком году вышел папку?"

gen_text = "Искусственный интеллект меняет всё вокруг нас быстрее, чем мы успеваем это осознать. Сегодня разберём три главных инструмента, которые реально сэкономят ваше время."

output_dir = "/Users/artemcvetkov/Desktop/"

cmd = [
    "f5-tts_infer-cli",
    "--model", "F5TTS_v1_Base",
    "--ref_audio", ref_audio,
    "--ref_text", ref_text,
    "--gen_text", gen_text,
    "--output_dir", output_dir,
]

print("Генерую голос...")
result = subprocess.run(cmd, capture_output=False, text=True)
print("Готово! Перевір робочий стіл — файл infer_cli_out.wav")
