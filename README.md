# Song Solver

A Python application that allows users to sing in front of their laptop's microphone, processes the recording using the Whisper API, and then leverages a Large Language Model (LLM) to recognize the song.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/przadka/song-solver.git
   ```

2. Navigate to the project directory:
   ```
   cd song-solver
   ```

3. Create and activate a virtual environment (optional, but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Prerequisites

### Environment Variables

The program expects an environment variable named `OPENAI_API_KEY` to be set. This key is used to authenticate with the OpenAI API for song recognition.

To set the environment variable:

#### On Linux/macOS:

```bash
export OPENAI_API_KEY=your_api_key_here
```

#### On Windows (Command Prompt):

```bash
set OPENAI_API_KEY=your_api_key_here
```

#### On Windows (PowerShell):

```bash
$env:OPENAI_API_KEY = "your_api_key_here"
```

Replace `your_api_key_here` with your actual OpenAI API key.

After setting the environment variable, you can run the program as described in the [Usage](#usage) section.

## Usage

To run the program:
```bash
python main.py
```
Follow the on-screen prompts to record your song. The application will then attempt to recognize the song based on the provided recording.

## License

Open-source software licensed under the MIT License.

