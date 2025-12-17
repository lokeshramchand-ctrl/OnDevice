from audio.capture import stream_audio
from stt.whisper_runner import transcribe
from context.manager import ContextManager

ctx = ContextManager(max_minutes=3)

for wav in stream_audio(10):
    t = transcribe(wav)
    ctx.add_transcript(t["text"])
    ctx.extract(t["text"])
    ctx.trim()
