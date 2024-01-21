import logging
from django.utils import timezone

class MyLogger:
    def __init__(self, name, log_file='log.txt'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def log_with_timezone(self, level, message):
        timestamp = timezone.now().strftime('%Y-%m-%d %H:%M:%S %Z')
        log_message = f'{timestamp} - {level} - {message}'
        getattr(self.logger, level.lower())(log_message)





'''
if __name__ == "__main__":
    logger = MyLogger("my_logger")

    logger.log_with_timezone("DEBUG", "Debug message")
    logger.log_with_timezone("INFO", "Info message")
    logger.log_with_timezone("WARNING", "Warning message")
    logger.log_with_timezone("ERROR", "Error message")
    logger.log_with_timezone("CRITICAL", "Critical message")
'''