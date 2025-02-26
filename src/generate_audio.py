import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Replace these with your actual API key and voice ID from the environment variables
API_KEY = os.getenv('API_key')
VOICE_ID = os.getenv('Voise_id_Anika_Customer_Care_Agent')

# Your script text for TTS
text_to_convert = (
    "Namaste Mathangi! My name is Anika, and I’m here to guide you through managing your credit card dues. "
    "Mathangi, as of today, your credit card bill shows an amount due of INR 5,053, which needs to be paid by 31st December 2024. "
    "Missing this payment could lead to two significant consequences: first, a late fee will be added to your outstanding balance; "
    "and second, your credit score will be negatively impacted, which may affect your future borrowing ability. "
    "Make your payment by clicking the link here, and pay through UPI or bank transfer. Thank you!"
)

# Set headers for the API request
headers = {
    "Accept": "audio/mpeg",
    "xi-api-key": API_KEY,
    "Content-Type": "application/json"
}

# Configure voice settings with speed set to 0.92; other parameters are default
data = {
    "text": text_to_convert,
    "voice_settings": {
        "speed": 0.92
    }
}

# Make the API request to ElevenLabs
response = requests.post(
    f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}",
    headers=headers,
    json=data
)

# Define the output file path
output_file_path = "data/output_audio.mp3"

# Create directories if they do not exist
os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

# Save the generated audio to a file
if response.status_code == 200:
    with open(output_file_path, "wb") as f:
        f.write(response.content)
    print(f"Audio generated and saved as {output_file_path}")
else:
    print("Error:", response.status_code, response.text)