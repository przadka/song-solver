from audio_processing import recording, whisper_api
from llm_recognition import recognizer

def main():
    print("Starting...")
    # Capture audio from the user
    print("Capturing audio...")
    audio_path = recording.capture_audio()

    print(f"Audio captured to: {audio_path}")
    # Process audio using Whisper
    processed_audio = whisper_api.process_audio_with_whisper(audio_path)

    print(f"Transcript: {processed_audio}")

    # Recognize song using LLM
    song_name = recognizer.recognize_song(processed_audio)
    
    if song_name:
        print(f"Recognized song: {song_name}")
    else:
        print("Song not recognized.")

if __name__ == '__main__':
    main()
