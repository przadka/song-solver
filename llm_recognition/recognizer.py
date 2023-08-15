from openai import ChatCompletion

def recognize_song(processed_audio):
    """
    Recognizes the song from the processed audio using a large language model (LLM).
    
    Args:
    - processed_audio (str): Processed audio or transcription.
    
    Returns:
    - str: Recognized song name or None if not recognized.
    """
    system_prompt = "You are an expert in songs with perfect knowledge of titles, artists, release dates, and lyrics."

    try:
        response = ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"What song is this text from: \"{processed_audio}\". Output only the song title and artist name (when applicable) and nothing else."},
            ]
        )

        if 'choices' in response and response['choices'] and 'message' in response['choices'][0]:
            return response['choices'][0]['message']['content']
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None
