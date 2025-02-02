from elevenlabs import play
from elevenlabs.client import ElevenLabs

from config import ELEVEN_API_KEY
from logger import get_logger

logger = get_logger()




client = ElevenLabs(api_key=ELEVEN_API_KEY)

def text_to_speech(text: str, voice_id="9BWtsMINqrJLrRacOk9x", model_id="eleven_multilingual_v2"):
    """
    Convert text to speech using ElevenLabs API.

    :param text: The text to convert to speech.
    :param voice_id: The voice ID (default is Bella's ID).
    :param model_id: The model to use (default is multilingual v2).
    """
    try:
        logger.info(f"Generating speech for: {text}")

        audio = client.text_to_speech.convert(
            text=text,
            voice_id=voice_id,
            model_id=model_id,
            output_format="mp3_44100_128",
        )

        play(audio)
        logger.info("Audio played successfully.")

    except Exception as e:
        logger.error(f"Error generating speech: {e}")
