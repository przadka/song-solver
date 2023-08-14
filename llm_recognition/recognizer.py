import openai

def recognize_song(processed_audio):
    """
    Recognizes the song from the processed audio using a large language model (LLM).
    
    Args:
    - processed_audio (str): Processed audio or transcription.
    
    Returns:
    - str: Recognized song name or None if not recognized.
    """
    prompt = "You are an expert in songs with perfect knowledge of songs, titles, release dates, and lyrics."

    response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": "What song is this text from:\""+processed_audio+"\". Output only the song title and artist name (when applicable) and nothing else."},
        ]
    )

    return response['choices'][0]['message']['content']



