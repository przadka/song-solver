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

## Usage

To run the program:
```bash
python main.py
```
Follow the on-screen prompts to record your song. The application will then attempt to recognize the song based on the provided recording.

## License

Open-source software licensed under the MIT License.

