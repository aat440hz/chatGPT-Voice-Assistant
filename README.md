# Voice Assistant

Welcome to our customizable voice assistant utilizing OpenAI's GPT-3.5 model. This assistant aims to provide an interactive and responsive AI companion, able to understand and respond to a variety of queries and commands.

## Installation

Before getting started, ensure Python 3.x is installed on your system.

1. **Python Dependencies**: Run `pip install -r requirements.txt` to install necessary Python packages.
2. **System-level Dependencies**: Certain functionalities require additional installations:
   - `sudo apt-get install flac` for FLAC audio codec, crucial for speech recognition features.
   - `sudo apt-get install portaudio19-dev` for PyAudio, necessary for audio input and output.
   - `sudo apt-get install espeak` for pyttsx3, a text-to-speech conversion library.

## Usage

*You will need an OpenAI API key which needs to be included in the code for this to work!*
Execute `python3 chatgpt_voice_assistant.py` from your terminal to start the assistant. Ensure your microphone is properly configured and working. Speak "Meatball" to activate the assistant and begin interaction.

## Contribution

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

## License

Distributed under the MIT License. See `LICENSE` for more information.
