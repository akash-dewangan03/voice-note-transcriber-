import requests
import time
import os

class AudioToText:
    @staticmethod
    def transcribe_audio(file, api_key):
        headers = {
            'authorization': api_key,
            'content-type': 'application/json'
        }

        # 🔹 Upload the audio file
        upload_url = "https://api.assemblyai.com/v2/upload"
        upload_response = requests.post(upload_url, headers=headers, files={'file': file})

        if upload_response.status_code != 200:
            return "❌ Failed to upload audio. Check API Key or network."

        try:
            audio_url = upload_response.json().get('upload_url', None)
            if not audio_url:
                return "❌ No audio URL returned. AssemblyAI error."
        except requests.exceptions.JSONDecodeError:
            return "❌ Failed to decode API response."

        # 🔹 Request transcription
        transcription_request = {'audio_url': audio_url}
        transcribe_url = "https://api.assemblyai.com/v2/transcript"
        transcribe_response = requests.post(transcribe_url, json=transcription_request, headers=headers)

        if transcribe_response.status_code != 200:
            return "❌ Failed to submit transcription request."

        try:
            transcript_id = transcribe_response.json().get('id', None)
            if not transcript_id:
                return "❌ Transcription request failed."
        except requests.exceptions.JSONDecodeError:
            return "❌ Failed to decode transcription response."

        # 🔹 Poll for transcription result
        while True:
            transcript_url = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"
            transcript_response = requests.get(transcript_url, headers=headers)
            transcript = transcript_response.json()

            if transcript['status'] == 'completed':
                return transcript['text']
            elif transcript['status'] == 'failed':
                return "❌ Transcription failed."
            else:
                time.sleep(5)
