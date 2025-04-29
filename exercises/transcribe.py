AUTH_TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJwYXRyaWNrY21kIiwiYWNjb3VudF90eXBlIjoiRnJlZSIsImV4cCI6NDg2OTE4NjUzOX0.wcFG_GjBSNVZCpP4NPC2xk6Dio8Jdd8vMb8e_rzXOFc"

import os
import requests
from pydub import AudioSegment
from dotenv import load_dotenv

# Load API token from .env
load_dotenv()
ACCESS_TOKEN = os.getenv("AUTH_TOKEN")

# Sunbird STT API endpoint
STT_URL = "https://api.sunbird.ai/tasks/stt"

# Supported languages and their codes
LANGUAGE_CODES = {
    "English": "eng",
    "Luganda": "lug",
    "Runyankole": "nyn",
    "Ateso": "teo",
    "Lugbara": "lgg",
    "Acholi": "ach",
}

def get_audio_duration(file_path):
    try:
        audio = AudioSegment.from_file(file_path)
        return len(audio) / 1000  # in seconds
    except Exception as e:
        print(f"Error loading audio file: {e}")
        return None

def transcribe_audio(file_path, lang_code):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    }

    files = {
        "audio": (
            os.path.basename(file_path),
            open(file_path, "rb"),
            "audio/mpeg",  # adjust if using WAV or other formats
        ),
    }

    data = {
        "language": lang_code,
        "adapter": lang_code,
    }

    try:
        response = requests.post(STT_URL, headers=headers, files=files, data=data)
        response.raise_for_status()
        return response.json().get("text", "No transcription returned.")
    except Exception as e:
        return f"API error: {e}"

def main():
    print("Please provide path to the audio file (Audio length less than 5 minutes):")
    file_path = input("> ").strip()

    if not os.path.exists(file_path):
        print("Error: File not found.")
        return

    duration = get_audio_duration(file_path)
    if duration is None:
        return
    if duration > 300:
        print("Error: Audio file exceeds 5 minutes.")
        return

    print("Please choose the target language (English, Luganda, Runyankole, Ateso, Lugbara or Acholi):")
    user_lang = input("> ").strip().title()

    if user_lang not in LANGUAGE_CODES:
        print("Unsupported language.")
        return

    lang_code = LANGUAGE_CODES[user_lang]
    print(f"\nTranscribing audio in {user_lang}... Please wait.")

    result = transcribe_audio(file_path, lang_code)
    print(f"\nAudio transcription text in {user_lang.lower()}:\n{result}")

if __name__ == "__main__":
    main()
