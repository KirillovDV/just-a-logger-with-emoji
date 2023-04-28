import logging


class EmojiLogger(logging.Logger):
    def __init__(self, name, level=logging.DEBUG):
        super().__init__(name, level)
        self._add_emoji()

    def _add_emoji(self):
        logging.addLevelName(logging.DEBUG, "🔍 DEBUG")
        logging.addLevelName(logging.INFO, "ℹ️ INFO")
        logging.addLevelName(logging.WARNING, "⚠️ WARNING")
        logging.addLevelName(logging.ERROR, "❌ ERROR")
        logging.addLevelName(logging.CRITICAL, "🚨 CRITICAL")
        logging.addLevelName(15, "🔧 CREATING")  # добавлен уровень "Creating" с уровнем 15

        formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        self.addHandler(handler)

    def creating(self, message):
        self.log(15, message)


logger = EmojiLogger(__name__)

# ----- HOW TO USE ------

# from logger import logger
#
# logger.debug("Debug message")
# logger.info("Info message")
# logger.warning("Warning message")
# logger.error("Error message")
# logger.critical("Critical message")
# logger.creating("Creating message")
