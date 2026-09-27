# ai_backend.py
import os
import tempfile
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError


load_dotenv()

class GeminiAssistant:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError(".env file does not contain GEMINI_API_KEY or it's empty.")
        
        self.client = genai.Client(api_key=self.api_key)

    def upload_file_to_gemini(self, uploaded_file):
        
        
        try:
            suffix = os.path.splitext(uploaded_file.name)[1]
            with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                tmp_path = tmp_file.name


            gemini_file = self.client.files.upload(file=tmp_path)
            os.remove(tmp_path)  
            return gemini_file
        except Exception as e:
            raise Exception(f"File upload error: {e}")

    def generate_response_stream(self, prompt, gemini_file=None,model="models/gemini-flash-lite-latest", temperature=0.7):
       
        contents = []
        if gemini_file:
            contents.append(gemini_file)
        contents.append(prompt)

        try:
          response = self.client.models.generate_content_stream(
            model=model,
            contents=contents,
            config={
                "temperature": temperature
            }
            )
          for chunk in response:
                if chunk.text:
                    yield chunk.text
        except APIError as e:
            if e.code == 429 or "RESOURCE_EXHAUSTED" in str(e):
                yield "\n[Error: Request Limit exceeded.]"
            else:
                yield f"\n[API Error: {e}]"
        except Exception as e:
            yield f"\n[Error: {e}]"