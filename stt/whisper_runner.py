import subprocess
from datetime import datetime

WHISPER_BIN = "./whisper.cpp/main"
MODEL_PATH = "./whisper.cpp/models/ggml-small.bin"

def transcribe(audio_path: str):
    result = subprocess.run(
        [WHISPER_BIN, "-m", MODEL_PATH, "-f", audio_path],
        capture_output=True,
        text=True
    )

    return {
        "timestamp": datetime.now().isoformat(),
        "text": result.stdout.strip()
    }

