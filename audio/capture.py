import sounddevice as sd
import numpy as np
import wave
import time

SAMPLE_RATE = 16000
CHANNELS = 1

def record_chunk(seconds: int, output_path: str):
    audio = sd.rec(
        int(seconds * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="int16"
    )
    sd.wait()

    with wave.open(output_path, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(audio.tobytes())

def stream_audio(chunk_seconds=10):
    while True:
        filename = f"chunk_{int(time.time())}.wav"
        record_chunk(chunk_seconds, filename)
        yield filename
