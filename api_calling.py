from google import genai
import os
from dotenv import load_dotenv

# laoding the environment variables
load_dotenv()

my_api_key = os.environ.get("GEMINI_API_KEY")

# api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key= my_api_key)


def note_generator(photos):

    prompt = """Summarize the picture in at max 100 words, make sure to add markdown
    to differentiate different sections """

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[photos, prompt],
    )

    return response.text

from gtts import gTTS
import io

def audio_transcription(notes):
    speech = gTTS(notes, lang = "en", slow= False)

    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)

    return audio_buffer

def quiz_generator(photos, difficulty):
    prompt = f"Generate 3 quizes based on {difficulty}. Make sure to add markdown to differentiate the options.Show the answers in below section, not with the question."

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[photos, prompt],
    )

    return response.text