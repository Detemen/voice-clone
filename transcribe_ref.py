import whisper

model = whisper.load_model("base")

files = [
    "/Users/artemcvetkov/Desktop/Новий запис 4.m4a",
    "/Users/artemcvetkov/Desktop/Новий запис 5.m4a",
    "/Users/artemcvetkov/Desktop/Новий запис 6.m4a",
    "/Users/artemcvetkov/Desktop/Новий запис 7.m4a",
]

for f in files:
    result = model.transcribe(f, language="ru")
    name = f.split("/")[-1]
    print(f"\n=== {name} ===")
    print(result["text"].strip())
