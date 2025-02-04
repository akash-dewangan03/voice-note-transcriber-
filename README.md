# Voice Note Transcriber 🔉💬

**Voice Note Transcriber** is a web application built using **Streamlit** that allows users to upload audio files (in `wav` or `mp3` format), transcribe them into text, and generate concise summaries. The app uses the **AssemblyAI API** for transcription and **Hugging Face's BART model** for text summarization. Users can download the full transcription and summary in `.txt` or `.docx` formats.

---

## Features

- **Audio Upload**: Upload your audio files in `wav` or `mp3` format.
- **Audio Transcription**: Convert uploaded audio into text using the **AssemblyAI API**.
- **Text Summarization**: Get a bullet-point summary of the transcription using **Hugging Face’s BART model**.
- **Export Options**:
  - Download the full transcription as a `.txt` file.
  - Download the summary as a `.txt` or `.docx` file.

---

## Installation

To run this project locally, follow these steps:

1. Clone the repository
  
    ```bash
    git clone https://github.com/akash-dewangan03/voice-note-transcriber-.git
    cd voice-note-transcriber-

2. Set up a virtual environment

     ```bash
     python -m venv venv
     source venv/bin/activate  # For macOS/Linux
     venv\Scripts\activate  # For Windows

3. Install dependencies

     ```bash
     pip install -r requirements.txt

4. Set up API keys
    - You will need an AssemblyAI API key for transcription services.
    - Create a .env file in the root of the project and add the following

    ```bash
    ASSEMBLYAI_API_KEY=your_api_key_here

5. Run the app

    ```bash
    streamlit run streamlitApp.py

- The app will open in your browser. You can now upload audio files, get transcriptions, and summaries!


## Technologies Used

- **Streamlit**: Used for building the interactive web interface.
- **AssemblyAI API**: Provides the speech-to-text functionality to transcribe audio files into text.
- **Hugging Face Transformers**: Utilized for text summarization, specifically using the BART model.
- **python-docx**: Generates `.docx` files from the summarized text.
- **Requests**: Handles HTTP requests to interact with the APIs.
- **dotenv**: Manages environment variables securely for API keys and sensitive data.

## Acknowledgements

- **AssemblyAI**: For providing the speech-to-text API.
- **Hugging Face**: For the BART model used for summarization.
- **Streamlit**: For creating a simple and easy-to-use framework for building web apps.

