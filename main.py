from chat_lexi import ChatLexi
from logger import get_logger
from text_to_speech import text_to_speech
from wake_words_detector import WakeWordsDetector

logger = get_logger()


wake_words = ["hey lexi", "hello lexi", "lexi"]

wake_detector = WakeWordsDetector(wake_words)
lexi = ChatLexi()

if __name__ == "__main__":

    while True:
        if wake_detector.listen_for_wake_word():
            logger.info("Wake word detected")
            res = lexi.chat("Lexi initiate")
            text_to_speech(res["response"])

