import os
import sounddevice as sd
import numpy as np
from pydub import AudioSegment

def capture_audio(duration=10, filename="recorded_audio.mp3", rate=44100):
    """
    Captures audio from the user's microphone for the specified duration and saves as MP3.
    
    Args:
    - duration (int): Duration in seconds for which to capture audio.
    - filename (str): Name of the file where the audio will be saved.
    - rate (int): Sampling rate.
    
    Returns:
    - str: Path to the saved audio file.
    """
    
    # Capture audio
    audio_data = sd.rec(int(duration * rate), samplerate=rate, channels=2, dtype=np.int16)
    sd.wait()  # Wait for the recording to finish

    # Convert numpy array to audio segment
    audio_segment = AudioSegment(
        audio_data.tobytes(),
        frame_rate=rate,
        sample_width=audio_data.dtype.itemsize,
        channels=2
    )

    # Save audio segment to MP3
    audio_segment.export(filename, format="mp3")

    return filename
