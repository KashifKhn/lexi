import speech_recognition as sr

from logger import get_logger

logger = get_logger()


class WakeWordsDetector:
    def __init__(self, wake_words):
        self.wake_words = [word.lower() for word in wake_words]
        self.recognizer = sr.Recognizer()

    def listen_for_wake_word(self):
        with sr.Microphone() as source:
            print("source:", source)
            logger.info("Listening for wake words")
            self.recognizer.adjust_for_ambient_noise(source)
            try: 
                audio = self.recognizer.listen(source)
                print("audio:", audio)
                if not audio:
                    logger.error("No audio detected")
                    return False
                text = self.recognizer.recognize_google(audio).lower()  # type: ignore
                logger.info(f"Recognize text: {text}")
                for word in self.wake_words:
                    if word in text:
                        logger.info(f"Detected wake word are founded: {word}")
                        return True
            except sr.UnknownValueError:
                logger.error("Could not understand audio")
            except sr.RequestError as e:
                logger.error(f"Could not request results; {e}")

            return False
