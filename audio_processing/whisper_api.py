import os
import openai

def process_audio_with_whisper(audio_path):
    """
    Processes the given audio using the Whisper API.
    
    Args:
    - audio_path (str): Path to the audio file to process.
    
    Returns:
    - str: Processed audio or transcription.
    """
    model_id = 'whisper-1'

    audio_file = open(audio_path, 'rb')

    response = openai.Audio.transcribe(
        api_key=os.getenv('OPENAI_API_KEY'),
        model=model_id,
        file=audio_file
    )

    return response['text']